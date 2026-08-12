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

        st.title("🎓 EduAgent AI")

        st.divider()

        st.subheader("📄 Documentos")

        if "rag_initialized" not in st.session_state:
            st.session_state.rag_initialized = False

        if "document_name" not in st.session_state:
            st.session_state.document_name = "Nenhum"

        uploaded_file = st.file_uploader(
            "Carregar documento PDF",
            type=["pdf"],
        )

        if uploaded_file is not None:

            if st.button(
                "📥 Indexar documento",
                use_container_width=True,
            ):

                with st.spinner(
                    "Carregando e indexando documento..."
                ):

                    try:
                        # O arquivo enviado é armazenado apenas
                        # temporariamente. O fixture de testes
                        # versionado no Git não é alterado.
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

                        # Limpa o histórico quando um novo
                        # documento é indexado.
                        st.session_state.messages = []

                        st.success(
                            "Documento indexado com sucesso!"
                        )

                    except Exception as error:

                        st.error(
                            f"Erro ao indexar documento: {error}"
                        )

        st.divider()

        st.subheader("ℹ️ Informações")

        st.metric(
            label="Modelo",
            value=settings.MODEL_NAME,
        )

        status = (
            "🟢 Online"
            if st.session_state.rag_initialized
            else "🟡 Aguardando documento"
        )

        st.metric(
            label="Status",
            value=status,
        )

        document_name = st.session_state.document_name

        st.metric(
            label="Documento",
            value=(
                "Carregado"
                if document_name != "Nenhum"
                else "Nenhum"
            ),
        )

        if document_name != "Nenhum":
            st.caption(
                f"📄 {document_name}"
            )

        st.divider()

        if st.button(
            "🗑️ Limpar conversa",
            use_container_width=True,
        ):
            st.session_state.messages = []
            st.rerun()