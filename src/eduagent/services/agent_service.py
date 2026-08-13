"""Serviço responsável pelo agente EduAgent AI."""

from typing import Any

from langgraph.prebuilt import create_react_agent

from eduagent.services.llm_service import LLMService
from eduagent.tools.rag_tool import search_documents


class AgentService:
    """Coordena o agente ReAct do EduAgent AI."""

    SYSTEM_PROMPT = """
Você é o EduAgent AI, um assistente educacional baseado em documentos.

REGRAS OBRIGATÓRIAS:

1. Para responder perguntas relacionadas aos documentos, SEMPRE utilize
a ferramenta `search_documents`.

2. Responda EXCLUSIVAMENTE com informações encontradas nos documentos
fornecidos pela ferramenta.

3. NÃO utilize conhecimento próprio, conhecimento geral ou informações
externas aos documentos.

4. Se a ferramenta não encontrar informações relevantes para a pergunta,
responda claramente que a informação não foi encontrada nos documentos
disponíveis.

5. Nunca invente, complete ou suponha informações que não estejam nos
documentos.

6. Responda sempre em português.

7. Seja claro, objetivo e didático.

8. Quando a pergunta não puder ser respondida com os documentos,
não tente responder utilizando conhecimento geral.

9. Quando a ferramenta fornecer uma fonte, preserve essa informação
na resposta final.

10. Não invente páginas, nomes de arquivos ou fontes.

11. O histórico da conversa serve apenas para compreender o contexto
da pergunta atual. Para obter informações sobre o documento, faça uma
nova busca usando `search_documents`.

12. Nunca reutilize ou invente resultados de ferramentas de mensagens
anteriores.

Quando a ferramenta retornar informações relevantes, utilize SOMENTE
essas informações para construir a resposta final.
"""

    def __init__(
        self,
        llm_service: LLMService | None = None,
    ):
        self.llm_service = llm_service or LLMService()

        self.agent = create_react_agent(
            model=self.llm_service.llm,
            tools=[search_documents],
            prompt=self.SYSTEM_PROMPT,
        )

    def invoke(
        self,
        input_data: str | dict[str, Any],
    ):
        """
        Executa o agente.

        Aceita:
        - uma pergunta como string;
        - um estado LangGraph no formato {"messages": [...]}.

        Retorna o estado final do agente.
        """

        if isinstance(input_data, str):
            payload = {
                "messages": [
                    {
                        "role": "user",
                        "content": input_data,
                    }
                ]
            }

        elif isinstance(input_data, dict):
            if "messages" not in input_data:
                raise ValueError(
                    "O estado do agente deve conter a chave 'messages'."
                )

            payload = input_data

        else:
            raise TypeError(
                "input_data deve ser uma string ou um dicionário "
                "contendo 'messages'."
            )

        return self.agent.invoke(payload)

    def ask(self, question: str) -> str:
        """
        Faz uma pergunta ao agente e retorna somente a resposta final.
        """

        result = self.ask_with_sources(question)

        return result["answer"]

    def ask_with_sources(
        self,
        question: str,
        conversation_history: list[dict[str, str]] | None = None,
    ) -> dict[str, Any]:
        """
        Faz uma pergunta ao agente e retorna a resposta juntamente
        com as fontes encontradas durante a busca.

        O histórico é utilizado somente como contexto textual.
        As mensagens internas de ferramentas não são reutilizadas.

        Retorna:
            {
                "answer": str,
                "sources": list[dict]
            }
        """

        if not isinstance(question, str):
            raise TypeError(
                "A pergunta deve ser uma string."
            )

        question = question.strip()

        if not question:
            raise ValueError(
                "A pergunta não pode estar vazia."
            )

        messages = []

        # ---------------------------------------------------------
        # Histórico textual da conversa
        # ---------------------------------------------------------

        if conversation_history:

            history_lines = []

            for message in conversation_history:

                role = message.get("role")
                content = message.get("content", "")

                if role not in {"user", "assistant"}:
                    continue

                if not isinstance(content, str):
                    continue

                content = content.strip()

                if not content:
                    continue

                # Evita colocar detalhes técnicos ou fontes completas
                # novamente no contexto do agente.
                history_lines.append(
                    f"{'Usuário' if role == 'user' else 'Assistente'}: "
                    f"{content}"
                )

            if history_lines:

                history_text = "\n".join(history_lines)

                messages.append(
                    {
                        "role": "user",
                        "content": (
                            "Contexto da conversa anterior:\n\n"
                            f"{history_text}\n\n"
                            "Agora responda à nova pergunta abaixo. "
                            "Use o histórico somente para compreender "
                            "o contexto. Para informações do documento, "
                            "faça uma nova busca em `search_documents`.\n\n"
                            f"Nova pergunta: {question}"
                        ),
                    }
                )

            else:
                messages.append(
                    {
                        "role": "user",
                        "content": question,
                    }
                )

        else:
            messages.append(
                {
                    "role": "user",
                    "content": question,
                }
            )

        response = self.invoke(
            {
                "messages": messages,
            }
        )

        response_messages = response.get(
            "messages",
            [],
        )

        if not response_messages:
            return {
                "answer": "O agente não retornou nenhuma mensagem.",
                "sources": [],
            }

        answer = ""

        # Procura a resposta final do agente.
        # Mensagens da ferramenta RAG não devem ser exibidas diretamente.
        for message in reversed(response_messages):

            message_type = getattr(
                message,
                "type",
                None,
            )

            if message_type != "ai":
                continue

            content = getattr(
                message,
                "content",
                None,
            )

            if not isinstance(content, str):
                continue

            content = content.strip()

            if not content:
                continue

            # Remove linhas de fonte caso o modelo tenha repetido a fonte
            # na resposta final.
            lines = content.splitlines()

            cleaned_lines = [
                line
                for line in lines
                if not line.strip().lower().startswith("fonte:")
            ]

            cleaned_content = "\n".join(
                cleaned_lines
            ).strip()

            if cleaned_content:
                answer = cleaned_content
                break

        if not answer:
            answer = (
                "O agente não retornou uma resposta válida."
            )
        sources = self._extract_sources(
            response_messages
        )
        return {
            "answer": answer,
            "sources": sources,
        }

    @staticmethod
    def _extract_sources(
        messages: list[Any],
    ) -> list[dict[str, Any]]:
        """
        Extrai fontes das mensagens retornadas pela ferramenta RAG.
        """

        sources = []
        seen = set()

        for message in messages:

            content = getattr(
                message,
                "content",
                None,
            )

            if not isinstance(content, str):
                continue

            if "Fonte:" not in content:
                continue

            blocks = content.split("---")

            for block in blocks:

                lines = [
                    line.strip()
                    for line in block.splitlines()
                    if line.strip()
                ]

                source_line = next(
                    (
                        line
                        for line in lines
                        if line.startswith("Fonte:")
                    ),
                    None,
                )

                if not source_line:
                    continue

                source_text = source_line.replace(
                    "Fonte:",
                    "",
                    1,
                ).strip()

                if not source_text:
                    continue

                page = None

                if " — página " in source_text:

                    source_name, page_text = source_text.rsplit(
                        " — página ",
                        1,
                    )

                    try:
                        page = int(page_text)

                    except ValueError:
                        page = None

                else:
                    source_name = source_text

                key = (
                    source_name,
                    page,
                )

                if key in seen:
                    continue

                seen.add(key)

                sources.append(
                    {
                        "name": source_name,
                        "page": page,
                    }
                )

        return sources

