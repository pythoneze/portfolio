import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1 , col2 = st.columns(2)

with col1:
    st.image("images/photo.png")
    
with col2:
    st.title("Ezequiel González Lagos")
    introduction = """
        Hi, I am Ezequiel! I am a Python programmer. I am a self-taught developer. 
    """
    st.info(introduction)

text = """
    Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(text)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])