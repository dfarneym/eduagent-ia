"""
Interface principal de conversação do EduAgent AI.
"""

import streamlit as st

from eduagent.services.agent_service import AgentService


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

        document_name = st.session_state.get(
            "document_name",
            "Documento",
        )

        st.markdown(
            "### 💬 Assistente Educacional"
        )

        st.caption(
            f"Faça perguntas sobre **{document_name}**."
        )

        st.markdown(
            "**Sugestões de perguntas:**"
        )

        suggestions = [
            "Qual é o objetivo deste documento?",
            "Quais são os principais pontos apresentados?",
            "Explique um conceito encontrado no texto.",
        ]

        cols = st.columns(3)

        for index, suggestion in enumerate(suggestions):

            with cols[index]:

                if st.button(
                    suggestion,
                    use_container_width=True,
                    key=f"suggestion_{index}",
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