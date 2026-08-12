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

.block-container {
    max-width: 1200px;
    padding-top: 1.5rem;
    padding-bottom: 3rem;
}

/* =====================================================
   Cabeçalho
===================================================== */

.hero {
    padding: 0.5rem 0 1rem 0;
}

.hero-title {
    font-size: 2.15rem;
    font-weight: 700;
    letter-spacing: -0.03em;
    margin-bottom: 0.2rem;
}

.hero-subtitle {
    font-size: 0.98rem;
    opacity: 0.65;
    margin-bottom: 0.8rem;
}

/* =====================================================
   Documento ativo
===================================================== */

.document-status {
    display: inline-flex;
    align-items: center;
    gap: 0.45rem;
    padding: 0.35rem 0.7rem;
    border: 1px solid rgba(128, 128, 128, 0.22);
    border-radius: 999px;
    font-size: 0.82rem;
    line-height: 1.2;
    opacity: 0.85;
}

/* =====================================================
   Card inicial
===================================================== */

.welcome-card {
    padding: 1.1rem 1.2rem;
    border: 1px solid rgba(128, 128, 128, 0.22);
    border-radius: 14px;
    margin: 0.5rem 0 1.25rem 0;
}

.welcome-title {
    font-weight: 650;
    font-size: 1.05rem;
    margin-bottom: 0.5rem;
}

.welcome-text {
    opacity: 0.75;
    font-size: 0.92rem;
    line-height: 1.5;
}

/* =====================================================
   Chat
===================================================== */

[data-testid="stChatMessage"] {
    border-radius: 14px;
    margin-bottom: 0.75rem;
}

[data-testid="stChatInput"] {
    margin-top: 1rem;
}

/* =====================================================
       Sugestões de perguntas
===================================================== */

[data-testid="stHorizontalBlock"] .stButton > button {
        min-height: 3.2rem;
        height: 3.2rem;
        padding: 0.45rem 0.7rem;
        font-size: 0.82rem;
        line-height: 1.25;
        border-radius: 10px;
        white-space: normal;
}

/* =====================================================
   Sidebar
===================================================== */

section[data-testid="stSidebar"] {
    border-right: 1px solid rgba(128, 128, 128, 0.2);
}

section[data-testid="stSidebar"] .block-container {
    padding-top: 1.5rem;
}

/* =====================================================
   Interface Streamlit
===================================================== */

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

    # =========================================================
    # Cabeçalho principal
    # =========================================================

    st.markdown(
        """
<div class="hero">
    <div class="hero-title">🎓 EduAgent AI</div>
    <div class="hero-subtitle">Assistente educacional inteligente</div>
</div>
        """,
        unsafe_allow_html=True,
    )

    # =========================================================
    # Status do documento
    # =========================================================

    if not st.session_state.rag_initialized:
        st.markdown(
            """
<div class="welcome-card">
    <div class="welcome-title">
        👋 Bem-vindo ao EduAgent AI
    </div>
    <div class="welcome-text">
        Carregue e indexe um documento PDF na
        barra lateral para começar a fazer
        perguntas sobre o conteúdo.
    </div>
</div>
            """,
            unsafe_allow_html=True,
        )

    else:
        document_name = st.session_state.document_name

        st.markdown(
            f"""
<div class="welcome-card">
    <div class="welcome-title">
        📄 Documento ativo
    </div>
    <div class="welcome-text">
        {document_name}
    </div>
</div>
            """,
            unsafe_allow_html=True,
        )

    # =========================================================
    # Chat
    # =========================================================

    render_chat()