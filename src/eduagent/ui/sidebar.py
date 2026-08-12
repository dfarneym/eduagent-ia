"""
Barra lateral do EduAgent AI.

Responsável pelo carregamento e indexação dos documentos.
"""

import tempfile
from pathlib import Path

import streamlit as st

from eduagent.config.settings import settings
from eduagent.tools.rag_tool import initialize_rag


def render_sidebar() -> None:
    """Renderiza a barra lateral."""

    with st.sidebar:

        st.markdown(
            """
            <div style="
                font-size: 1.45rem;
                font-weight: 700;
                margin-bottom: 0.25rem;
            ">
                🎓 EduAgent AI
            </div>

            <div style="
                font-size: 0.82rem;
                opacity: 0.65;
                margin-top: 0.25rem;
                margin-bottom: 1rem;
            ">
                Assistente educacional inteligente
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.divider()

        st.subheader("📄 Documento")

        uploaded_file = st.file_uploader(
            "Selecione um arquivo PDF",
            type=["pdf"],
            help="Envie um documento para que o EduAgent possa consultá-lo.",
        )

        if uploaded_file is not None:

            st.caption(
                f"Arquivo selecionado: **{uploaded_file.name}**"
            )

            if st.button(
                "📥 Indexar documento",
                use_container_width=True,
                type="secondary",
            ):
                with st.spinner(
                    "Carregando e indexando documento..."
                ):
                    try:
                        with tempfile.TemporaryDirectory() as temp_dir:

                            file_path = (
                                Path(temp_dir)
                                / uploaded_file.name
                            )

                            file_path.write_bytes(
                                uploaded_file.getbuffer()
                            )

                            initialize_rag(
                                str(file_path)
                            )

                        st.session_state.rag_initialized = True
                        st.session_state.document_name = (
                            uploaded_file.name
                        )

                        # O agente anterior pode ter sido criado
                        # com o estado anterior da aplicação.
                        st.session_state.agent = None

                        # Um novo documento começa uma nova conversa.
                        st.session_state.messages = []

                        st.success(
                            "Documento indexado com sucesso!"
                        )

                        st.rerun()

                    except Exception as error:

                        st.error(
                            f"Erro ao indexar documento: {error}"
                        )

        st.divider()

        st.subheader("📊 Status")

        if st.session_state.rag_initialized:
            st.success("Documento pronto para consulta")
        else:
            st.info("Aguardando documento")

        # Modelo com apresentação mais compacta.
        st.markdown(
            """
            <div style="
                margin-top: 1rem;
                margin-bottom: 0.25rem;
                font-size: 0.82rem;
                opacity: 0.65;
            ">
                Modelo
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div style="
                font-size: 0.95rem;
                font-weight: 600;
                line-height: 1.3;
                overflow: hidden;
                text-overflow: ellipsis;
                white-space: nowrap;
            "
            title="{settings.MODEL_NAME}">
                {settings.MODEL_NAME}
            </div>
            """,
            unsafe_allow_html=True,
        )

        document_name = st.session_state.document_name

        if document_name != "Nenhum":
            st.caption(
                "📄 Documento ativo"
            )

            st.markdown(
                f"""
                <div style="
                    font-size: 0.9rem;
                    font-weight: 600;
                    margin-top: -0.35rem;
                ">
                    {document_name}
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.caption(
                "📄 Nenhum documento carregado."
            )

        st.divider()

        st.subheader("⚙️ Controles")

        if st.button(
            "🗑️ Limpar conversa",
            use_container_width=True,
        ):
            st.session_state.messages = []
            st.rerun()

        st.divider()

        st.caption(
            "EduAgent AI · RAG + ReAct"
        )