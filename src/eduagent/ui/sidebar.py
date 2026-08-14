"""
Barra lateral do EduAgent AI.

Responsável pelo carregamento e indexação dos documentos.
"""

import tempfile
from pathlib import Path

import streamlit as st
from pypdf import PdfReader

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

        st.caption(
               f"Tamanho máximo: {settings.MAX_FILE_SIZE_MB} MB"
        )
        st.caption(
               f"📄 Máximo de páginas: {settings.MAX_PAGES}"
        )

        uploaded_file = st.file_uploader(
             "Selecione um arquivo PDF",
             type=["pdf"],
             max_upload_size=settings.MAX_FILE_SIZE_MB,
             help=(
                  f"PDF de até {settings.MAX_FILE_SIZE_MB} MB "
                  f"e {settings.MAX_PAGES} páginas."
           ),
        )

        if uploaded_file is not None:

            file_size_mb = uploaded_file.size / (1024 * 1024)

            st.caption(
                f"Arquivo selecionado: **{uploaded_file.name}**"
            )

            # -------------------------------------------------
            # Validação de tamanho
            # -------------------------------------------------

            file_size_valid = (
                uploaded_file.size
                <= settings.MAX_FILE_SIZE_MB * 1024 * 1024
            )

            # -------------------------------------------------
            # Validação de páginas
            # -------------------------------------------------

            page_count = None
            page_count_valid = True

            try:
                from io import BytesIO
                from pypdf import PdfReader

                reader = PdfReader(
                    BytesIO(uploaded_file.getvalue())
                )

                page_count = len(reader.pages)

                page_count_valid = (
                    page_count <= settings.MAX_PAGES
                )

            except Exception as error:
                page_count_valid = False

                st.error(
                    f"Não foi possível verificar o número de "
                    f"páginas do PDF: {error}"
                )

            # -------------------------------------------------
            # Informações do arquivo
            # -------------------------------------------------

            st.caption(
                f"📦 Tamanho: {file_size_mb:.2f} MB"
            )

            if page_count is not None:
                st.caption(
                    f"📄 Páginas: {page_count}"
                )

            # -------------------------------------------------
            # Mensagens de validação
            # -------------------------------------------------

            if not file_size_valid:

                st.error(
                    f"O arquivo excede o limite de "
                    f"{settings.MAX_FILE_SIZE_MB} MB."
                )

            elif not page_count_valid and page_count is not None:

                st.error(
                    f"O documento possui {page_count} páginas, "
                    f"mas o limite é de "
                    f"{settings.MAX_PAGES} páginas."
                )

            else:

                st.success(
                    "Documento dentro dos limites permitidos."
                )

            # -------------------------------------------------
            # Indexação
            # -------------------------------------------------

            can_index = (
                file_size_valid
                and page_count_valid
                and page_count is not None
            )

            if st.button(
                "📥 Indexar documento",
                use_container_width=True,
                type="secondary",
                disabled=not can_index,
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

                        st.session_state.agent = None

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