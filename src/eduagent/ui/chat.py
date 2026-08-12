"""
Interface principal de conversação do EduAgent AI.
"""

import streamlit as st

from eduagent.services.agent_service import AgentService


def render_chat() -> None:
    """Renderiza o histórico e a entrada do chat."""

    st.subheader("💬 Assistente Educacional")

    # Histórico da conversa
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Exibe mensagens anteriores
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Campo de pergunta
    question = st.chat_input(
        "Digite sua pergunta sobre os documentos..."
    )

    if not question:
        return

    # Exibe pergunta do usuário
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Verifica se existe documento indexado
    if not st.session_state.get("rag_initialized", False):
        response = (
            "Nenhum documento foi carregado ainda. "
            "Utilize a barra lateral para carregar um documento PDF."
        )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response,
            }
        )

        with st.chat_message("assistant"):
            st.markdown(response)

        return

    # Executa o agente
    with st.chat_message("assistant"):
        with st.spinner("Analisando os documentos..."):

            try:
                agent = AgentService()
                response = agent.ask(question)

            except Exception as error:
                response = (
                    "Ocorreu um erro ao processar sua pergunta.\n\n"
                    f"Detalhes: `{error}`"
                )

            st.markdown(response)

    # Salva resposta no histórico
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
        }
    )