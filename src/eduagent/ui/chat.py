"""Interface principal de conversação do EduAgent AI."""

import streamlit as st

from eduagent.services.agent_service import AgentService


def render_chat() -> None:
    """Renderiza o histórico e a entrada do chat."""

    # Histórico da conversa
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Histórico das mensagens
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

            # Mostra as fontes somente nas respostas do assistente
            if message["role"] == "assistant":
                sources = message.get("sources", [])

                if sources:
                    with st.expander("📚 Fontes consultadas"):
                        for source in sources:
                            name = source.get("name", "Documento")
                            page = source.get("page")

                            if page is not None:
                                st.markdown(
                                    f"📄 **{name}** — página {page}"
                                )
                            else:
                                st.markdown(
                                    f"📄 **{name}**"
                                )

    question = st.chat_input(
        "Digite sua pergunta sobre os documentos..."
    )

    if not question:
        return

    # Mostra a pergunta do usuário
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question,
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    # Verifica se existe documento indexado
    if not st.session_state.get(
        "rag_initialized",
        False,
    ):
        response = (
            "Nenhum documento foi carregado ainda. "
            "Utilize a barra lateral para carregar um documento PDF."
        )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response,
                "sources": [],
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

                result = agent.ask_with_sources(
                    question
                )

                response = result["answer"]
                sources = result.get(
                    "sources",
                    [],
                )

            except Exception as error:
                response = (
                    "Ocorreu um erro ao processar sua pergunta.\n\n"
                    f"Detalhes: `{error}`"
                )

                sources = []

            st.markdown(response)

            # Fontes da resposta atual
            if sources:
                with st.expander("📚 Fontes consultadas"):
                    for source in sources:
                        name = source.get(
                            "name",
                            "Documento",
                        )

                        page = source.get("page")

                        if page is not None:
                            st.markdown(
                                f"📄 **{name}** — página {page}"
                            )
                        else:
                            st.markdown(
                                f"📄 **{name}**"
                            )

    # Salva resposta e fontes no histórico
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
            "sources": sources,
        }
    )