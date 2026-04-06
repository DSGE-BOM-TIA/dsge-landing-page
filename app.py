from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="DSGE Landing Page", layout="wide")

st.markdown(
    '''
    <style>
    #MainMenu, header, footer {visibility: hidden;}
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 0rem;
        padding-right: 0rem;
        max-width: 100%;
    }
    iframe[title="streamlit_html"] {border: 0;}
    </style>
    ''',
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "landing.html"
html = html_path.read_text(encoding="utf-8")

components.html(html, height=3200, scrolling=True)
