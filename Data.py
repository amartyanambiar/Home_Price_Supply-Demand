import streamlit as st
import pandas as pd
import numpy as np
import datetime
import plotly.express as px

df = pd.read_csv('data/final_df.csv')

st.set_page_config(
    page_title="The Data",
)
col1, mid, col2 = st.columns([1, 3, 20])
with col1:
    st.image('public/logo.png', width=100)
with col2:
    st.markdown("""---""")
    st.markdown('### Technical Assessment - Amartya Nambiar')


st.markdown('### Problem Statement')
st.markdown('Build a model using publicly available data for key supply-demand factors that could influence US home prices. Use that to explain how these factors impacted home prices over the last ~20 years. ')


st.markdown('### The Data')
st.write(df)
