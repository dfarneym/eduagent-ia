"""
Página principal do EduAgent AI.

Responsável pela composição da interface.
"""

import streamlit as st

from eduagent.config.settings import settings
from eduagent.ui.chat import render_chat
from eduagent.ui.sidebar import render_sidebar


def inject_styles() -> None:
    """Aplica os estilos visuais da aplicação."""

    st.markdown(
        """
        <style>
        /* Área principal */
        .block-container {
            max-width: 1200px;
            padding-top: 2rem;
            padding-bottom: 3rem;
        }

        /* Cabeçalho */
        .hero {
            padding: 1.5rem 0 1rem 0;
        }

        .hero-title {
            font-size: 2.4rem;
            font-weight: 700;
            margin-bottom: 0.25rem;
        }

        .hero-subtitle {
            font-size: 1.05rem;
            opacity: 0.75;
            margin-bottom: 1.5rem;
        }

        /* Cards */
        .info-card {
            padding: 1.2rem;
            border: 1px solid rgba(128, 128, 128, 0.25);
            border-radius: 14px;
            margin-bottom: 1rem;
        }

        .info-card-title {
            font-weight: 650;
            font-size: 1rem;
            margin-bottom: 0.4rem;
        }

        .info-card-text {
            opacity: 0.75;
            font-size: 0.92rem;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            border-right: 1px solid rgba(128, 128, 128, 0.2);
        }

        section[data-testid="stSidebar"] .block-container {
            padding-top: 1.5rem;
        }

        /* Chat */
        [data-testid="stChatMessage"] {
            border-radius: 14px;
            margin-bottom: 0.75rem;
        }

        /* Input */
        [data-testid="stChatInput"] {
            margin-top: 1rem;
        }

        /* Esconde elementos desnecessários */
        #MainMenu {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def initialize_session_state() -> None:
    """Inicializa o estado da aplicação."""

    defaults = {
        "messages": [],
        "rag_initialized": False,
        "document_name": "Nenhum",
        "agent": None,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def run_app() -> None:
    """Inicializa e renderiza a aplicação."""

    st.set_page_config(
        page_title=settings.APP_NAME,
        page_icon="🎓",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    initialize_session_state()
    inject_styles()

    render_sidebar()

    st.markdown(
        """
        <div class="hero">
            <div class="hero-title">🎓 EduAgent AI</div>
            <div class="hero-subtitle">
                Plataforma inteligente para instituições de ensino
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if not st.session_state.rag_initialized:
        st.markdown(
            """
            <div class="info-card">
                <div class="info-card-title">
                    👋 Bem-vindo ao EduAgent AI
                </div>
                <div class="info-card-text">
                    Carregue um documento PDF na barra lateral para
                    começar a fazer perguntas sobre o conteúdo.
                    O sistema utiliza RAG para recuperar informações
                    diretamente dos documentos fornecidos.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div class="info-card">
                <div class="info-card-title">
                    📄 Documento ativo
                </div>
                <div class="info-card-text">
                    {st.session_state.document_name}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    render_chat()