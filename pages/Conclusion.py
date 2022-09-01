import streamlit as st
import pandas as pd
import numpy as np
import datetime
import plotly.express as px

df = pd.read_csv('data/final_df.csv')

col1, mid, col2 = st.columns([1, 3, 20])
with col1:
    st.image('public/logo.png', width=100)
with col2:
    st.markdown("""---""")
    st.markdown('###  Home Price Prediction')


st.markdown('### Conclusion')
st.markdown('In the task assigned, I had to build a model using publicly available data for key supply-demand factors that could influence US home prices. This involved collecting data from various sources and combining them into a single dataframe. The data was then cleaned and prepared for model building. The model was then built using the data and we calculated the r2 score of the model which was in the range of 0.7 - 1. I also used Streamlit to create a web application that would allow the user to input the features they wanted. Visualizations were created using Plotly Express, Seaborn and it is incorporated into the application.')

st.markdown("""---""")

st.markdown('### References')
st.write("[Scikit-Learn Docs](https://scikit-learn.org/stable/index.html)")
st.write("[Streamlit Docs](https://docs.streamlit.io)")
st.write("[Plotly Library](https://plotly.com/python/)")
st.write("[Personal Income](https://fred.stlouisfed.org/series/PI)")
st.write("[Home Price Index](https://fred.stlouisfed.org/series/CSUSHPISA)")
st.write("[New Constructions](https://www.census.gov/construction/nrc/historical_data/index.html)")
st.write("[New Permits](https://www.census.gov/construction/bps/)")
st.write("[GDP of USA](https://fred.stlouisfed.org/graph/?g=znfe)")
st.write("[Federal Fund Rate](https://fred.stlouisfed.org/series/DFF#0)")
st.write("[Mortgage Rate](https://fred.stlouisfed.org/graph/?g=zneW)")
