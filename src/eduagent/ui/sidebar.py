"""
Responsável apenas pela barra lateral.

Tudo que pertence à Sidebar ficará aqui.

"""

import streamlit as st

from eduagent.config.settings import settings


def render_sidebar() -> None:
    """Renderiza a barra lateral da aplicação."""

    with st.sidebar:

        st.title("🎓 EduAgent AI")

        st.divider()

        st.subheader("Informações")

        st.metric(# É um componente muito utilizado em dashboards.
            label="Modelo",
            value=settings.MODEL_NAME,
        )

        st.metric(
            label="Status",
            value="🟢 Online",
        )

        st.metric(
            label="Documentos",
            value="0",
        )