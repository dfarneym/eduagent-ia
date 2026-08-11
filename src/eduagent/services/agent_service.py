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

        2. Você deve responder EXCLUSIVAMENTE com informações encontradas
        nos documentos fornecidos pela ferramenta.

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

        EXEMPLO:

        Pergunta:
        "Qual é a capital da França?"

        Se os documentos não contiverem essa informação, NÃO responda:
        "Paris."

        Responda:
        "Não encontrei informações sobre a capital da França nos documentos disponíveis."

        Quando a ferramenta retornar informações relevantes, utilize SOMENTE essas
        informações para construir a resposta final.
        """
   
    def __init__(self, llm_service: LLMService | None = None):
        self.llm_service = llm_service or LLMService()

        self.agent = create_react_agent(
            model=self.llm_service.llm,
            tools=[search_documents],
            prompt=self.SYSTEM_PROMPT,
        )

    def invoke(self, input_data: str | dict[str, Any]):
        """
        Executa o agente.

        Aceita:
        - uma pergunta como string;
        - um estado LangGraph no formato {"messages": [...]}.

        Retorna:
            dict contendo o estado final do agente.
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

        if not isinstance(question, str):
            raise TypeError(
                "A pergunta deve ser uma string."
            )

        question = question.strip()

        if not question:
            raise ValueError(
                "A pergunta não pode estar vazia."
            )

        response = self.invoke(question)

        messages = response.get("messages", [])

        if not messages:
            return "O agente não retornou nenhuma mensagem."

        # Procura a última mensagem com conteúdo textual.
        for message in reversed(messages):
            content = getattr(message, "content", None)

            if isinstance(content, str) and content.strip():
                return content.strip()

        return "O agente não retornou uma resposta válida."

