import streamlit as st

st.set_page_config(layout="wide")

col1 , col2 = st.columns(2)

with col1:
    st.image("images/photo.png")
    
with col2:
    st.title("Ezequiel González")
    content = """
        Hi, I am Ezequiel! I am a Python programmer. I am a self-taught developer. 
    """
    st.info(content)

