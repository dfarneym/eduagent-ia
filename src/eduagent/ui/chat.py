"""
Interface principal de conversação do EduAgent AI.
"""

import streamlit as st

from eduagent.services.agent_service import AgentService


def get_agent() -> AgentService:
    """
    Retorna uma instância persistente do AgentService.

    O agente é armazenado no session_state para evitar
    sua recriação a cada pergunta.
    """

    if st.session_state.get("agent") is None:
        st.session_state.agent = AgentService()

    return st.session_state.agent


def render_empty_state() -> None:
    """Renderiza a mensagem inicial do chat."""

    st.info(
        """
        Faça perguntas sobre o documento carregado.

        **Exemplos:**

        - Qual é o objetivo deste documento?
        - Quais são os principais pontos apresentados?
        - Explique determinado conceito encontrado no texto.
        """
    )


def render_chat() -> None:
    """Renderiza o histórico e a entrada do chat."""

    st.subheader("💬 Assistente Educacional")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    if not st.session_state.messages:
        render_empty_state()

    # Histórico da conversa.
    for message in st.session_state.messages:

        role = message["role"]

        with st.chat_message(
            role,
            avatar="🎓" if role == "assistant" else "👤",
        ):
            st.markdown(message["content"])

    question = st.chat_input(
        "Digite sua pergunta sobre o documento..."
    )

    if not question:
        return

    question = question.strip()

    if not question:
        return

    # Salva e exibe a pergunta.
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message(
        "user",
        avatar="👤",
    ):
        st.markdown(question)

    # Verifica se existe documento indexado.
    if not st.session_state.get(
        "rag_initialized",
        False,
    ):

        response = (
            "📄 Nenhum documento foi carregado ainda.\n\n"
            "Utilize a barra lateral para carregar e indexar "
            "um documento PDF antes de fazer perguntas."
        )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response,
            }
        )

        with st.chat_message(
            "assistant",
            avatar="🎓",
        ):
            st.markdown(response)

        return

    # Executa o agente.
    with st.chat_message(
        "assistant",
        avatar="🎓",
    ):

        with st.spinner(
            "🔎 Consultando os documentos..."
        ):

            try:
                agent = get_agent()

                response = agent.ask(
                    question
                )

            except Exception as error:

                response = (
                    "⚠️ Ocorreu um erro ao processar sua pergunta.\n\n"
                    f"Detalhes: `{error}`"
                )

        st.markdown(response)

    # Salva a resposta.
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
        }
    )