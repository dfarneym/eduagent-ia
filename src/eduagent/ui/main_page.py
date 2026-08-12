"""
Página principal do EduAgent AI.

Responsável somente pela composição da interface.
"""

import streamlit as st

from eduagent.config.settings import settings
from eduagent.ui.chat import render_chat
from eduagent.ui.sidebar import render_sidebar


def run_app() -> None:
    """Inicializa e renderiza a aplicação."""

    st.set_page_config(
        page_title=settings.APP_NAME,
        page_icon="🎓",
        layout="wide",
    )

    # Inicializa estados da aplicação
    if "messages" not in st.session_state:
        st.session_state.messages = []

    if "rag_initialized" not in st.session_state:
        st.session_state.rag_initialized = False

    if "document_name" not in st.session_state:
        st.session_state.document_name = "Nenhum"

    # Barra lateral
    render_sidebar()

    # Cabeçalho
    st.title("🎓 EduAgent AI")

    st.subheader(
        "Plataforma Inteligente para Instituições de Ensino"
    )

    st.write(
        """
        Faça perguntas sobre os documentos carregados.
        O EduAgent AI utiliza RAG para recuperar informações
        dos documentos e um agente baseado em ReAct para
        construir as respostas.
        """
    )

    st.divider()

    # Interface de chat
    render_chat()