import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1 , col2 = st.columns(2)

with col1:
    st.image("images/photo.png")
    
with col2:
    st.title("Ezequiel González Lagos")
    introduction = """
        Hello! I'm Ezequiel, a Python programmer who has honed my skills through self-directed study. I'm enthusiastic about applying my programming knowledge to tackle challenges and create impactful solutions.
    """
    st.info(introduction)

st.write("Below, I will showcase my coding skills and projects.")

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")

midpoint = len(df) // 2 + len(df) % 2

for i, row in df.iterrows():
    column = col3 if i < midpoint else col4
    with column:
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")
