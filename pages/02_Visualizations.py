import streamlit as st
import pandas as pd
import numpy as np
import datetime
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/final_df.csv')


def pairplot(df):
    st.markdown('Pairplot')
    sns.set(style="ticks", color_codes=True)
    g = sns.pairplot(df)
    st.pyplot(g)


def visualize(f1):
    st.write(px.line(df, x="date", y=f1, width=1000, height=600,
                     title="Visualization over the last 20 years"))


def plot_corr(df):
    st.markdown(' Correlation Matrix')
    corr = df.corr()
    fig = px.imshow(corr, width=600, height=600,
                    color_continuous_scale=px.colors.sequential.Plasma)
    st.plotly_chart(fig)


st.set_page_config(
    page_title="Visualization",
)

col1, mid, col2 = st.columns([1, 3, 20])
with col1:
    st.image('public/logo.png', width=100)
with col2:
    st.markdown("""---""")
    st.markdown('### Technical Assessment - Amartya Nambiar')

st.markdown('### Visualizations')
st.markdown('Use the controls in the sidebar to visualize the data.')
st.markdown("""---""")

st.sidebar.title('Visualization Controls')
f1 = st.sidebar.selectbox('Select Y-axis feature', df.columns.drop('date'))

if (st.sidebar.button('Visualize')):
    visualize(f1)
st.sidebar.markdown('---')

st.sidebar.write("Understand Relation between Features")
if (st.sidebar.button('Heatmap')):
    plot_corr(df)

st.sidebar.markdown('---')

st.sidebar.write("Visualize in Pairplot  (might take a few seconds)")
if (st.sidebar.button('Pariplot')):
    pairplot(df)
