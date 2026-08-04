"""
Responsável por montar a tela.

Ele apenas organiza os componentes.

Nunca terá lógica de negócio.

"""
import streamlit as st

from eduagent.config.settings import settings
from eduagent.ui.sidebar import render_sidebar


def run_app():
    # Configurando a página
    st.set_page_config(
        page_title=settings.APP_NAME,
        page_icon="🎓",
        layout="wide"
    )

    render_sidebar()

    # O título da aplicação
    st.title("🎓 EduAgent AI")
    # O subtítulo da aplicação
    st.subheader("Plataforma Inteligente para Instituições de Ensino")

    st.write(
        """
        Bem-vindo ao EduAgent AI.

        Este agente utiliza IA e RAG para responder perguntas
        com base na documentação da instituição.
        """
    )