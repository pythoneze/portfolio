import streamlit as st
import pandas as pd

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

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")

for i, row in df.iterrows():
    column = col3 if i < len(df) // 2 else col4
    with column:
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")