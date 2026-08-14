"""
Interface principal de conversação do EduAgent AI.
"""

import streamlit as st

from eduagent.config.settings import settings
from eduagent.services.agent_service import AgentService

DEMO_QUESTIONS = {
    "01_manual_do_aluno.pdf": [
        "Como funciona o primeiro acesso?",
        "Como é registrada a frequência?",
        "Onde devo encaminhar dúvidas acadêmicas?",
    ],
    "02_matricula_e_acesso.pdf": [
        "Como funciona a matrícula?",
        "Como solicitar troca de turma?",
        "Como recuperar minha senha?",
    ],
    "03_bolsas_e_beneficios.pdf": [
        "Qual é o desconto da Bolsa de Desempenho?",
        "Qual pode ser o desconto da Bolsa Socioeconômica?",
        "Os benefícios podem ser acumulados?",
    ],
    "04_avaliacoes_e_recuperacao.pdf": [
        "Qual é a nota mínima para aprovação?",
        "Quem pode realizar recuperação?",
        "Como funciona a revisão de avaliação?",
    ],
    "05_certificados.pdf": [
        "Quais são os requisitos para receber o certificado?",
        "Onde o certificado digital é disponibilizado?",
        "Como solicitar uma segunda via?",
    ],
    "06_calendario_academico.pdf": [
        "Quando começam as aulas?",
        "Quando começam as avaliações finais?",
        "Quando serão divulgadas as notas?",
    ],
    "07_financeiro_e_pagamentos.pdf": [
        "Quais formas de pagamento são aceitas?",
        "O que acontece quando uma mensalidade está atrasada?",
        "Como solicitar uma negociação financeira?",
    ],
    "08_suporte_e_faq.pdf": [
        "Como recuperar minha senha?",
        "Onde vejo minhas notas?",
        "Onde encontro meu certificado?",
    ],
}

GENERIC_QUESTIONS = [
    "Qual é o objetivo deste documento?",
    "Quais são os principais pontos apresentados?",
    "Explique os principais conceitos do documento.",
    "Resuma o documento.",
]


def _render_sources(sources: list[dict]) -> None:
    """Renderiza as fontes consultadas pela resposta."""

    if not sources:
        return

    with st.expander("📚 Fontes consultadas"):
        for source in sources:
            name = source.get(
                "name",
                "Documento",
            )

            page = source.get("page")

            if page is not None:
                st.markdown(
                    f"📄 **{name}** · página {page}"
                )
            else:
                st.markdown(
                    f"📄 **{name}**"
                )


def _render_welcome() -> None:
    """Renderiza o estado inicial do chat."""

    if st.session_state.get("rag_initialized", False):

        document_name = st.session_state.document_name

        if document_name in DEMO_QUESTIONS:
            suggested_questions = DEMO_QUESTIONS[document_name]
        else:
            suggested_questions = GENERIC_QUESTIONS

        st.markdown("**💡 Sugestões de perguntas**")

        for suggestion in suggested_questions:
            if st.button(
                suggestion,
                key=f"suggestion_{suggestion}",
                use_container_width=True,
            ):
                st.session_state.suggested_question = suggestion
                st.rerun()

    else:

        st.markdown(
            "### 💬 Assistente Educacional"
        )

        st.info(
            "📄 Carregue e indexe um documento PDF "
            "na barra lateral para começar."
        )


def render_chat() -> None:
    """Renderiza o histórico e a entrada do chat."""

    # ---------------------------------------------------------
    # Estado inicial
    # ---------------------------------------------------------

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "suggested_question" not in st.session_state:
        st.session_state.suggested_question = None

    # ---------------------------------------------------------
    # Cabeçalho / estado inicial
    # ---------------------------------------------------------

    if not st.session_state.messages:
        _render_welcome()

    # ---------------------------------------------------------
    # Histórico da conversa
    # ---------------------------------------------------------

    for message in st.session_state.messages:

        role = message["role"]

        with st.chat_message(role):

            st.markdown(
                message["content"]
            )

            if role == "assistant":

                sources = message.get(
                    "sources",
                    [],
                )

                _render_sources(sources)

    # ---------------------------------------------------------
    # Entrada do usuário
    # ---------------------------------------------------------

    question = st.chat_input(
        "Faça uma pergunta sobre o documento..."
    )

    # Verifica se o usuário clicou em uma sugestão
    if not question:
        question = st.session_state.get(
            "suggested_question"
        )

    if not question:
        return

    question = question.strip()

    if len(question) > settings.MAX_QUESTION_CHARS:
        st.warning(
            f"A pergunta deve ter no máximo "
            f"{settings.MAX_QUESTION_CHARS} caracteres."
        )
        return

    # Limpa a sugestão depois de utilizá-la
    st.session_state.suggested_question = None

    # ---------------------------------------------------------
    # Histórico anterior à pergunta atual
    # ---------------------------------------------------------

    conversation_history = st.session_state.messages.copy()

    # ---------------------------------------------------------
    # Mensagem do usuário
    # ---------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # ---------------------------------------------------------
    # Verifica se existe documento indexado
    # ---------------------------------------------------------

    if not st.session_state.get(
        "rag_initialized",
        False,
    ):
        return

    # ---------------------------------------------------------
    # Executa o agente
    # ---------------------------------------------------------

    with st.chat_message("assistant"):

        with st.spinner(
            "Analisando o documento..."
        ):

            try:
                conversation_history = st.session_state.messages[
                      -settings.MAX_HISTORY_MESSAGES:
                ].copy()
                
                agent = AgentService()

                result = agent.ask_with_sources(
                    question,
                    conversation_history=conversation_history,
                )

                response = result.get(
                    "answer",
                    "O agente não retornou uma resposta.",
                )

                sources = result.get(
                    "sources",
                    [],
                )

            except Exception as error:

                response = (
                    "Não foi possível processar sua pergunta.\n\n"
                    f"Detalhes: `{error}`"
                )

                sources = []

        st.markdown(response)

        _render_sources(sources)

    # ---------------------------------------------------------
    # Salva resposta no histórico
    # ---------------------------------------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
            "sources": sources,
        }
    )