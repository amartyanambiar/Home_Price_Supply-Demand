import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
import pickle


df = pd.read_csv('data/final_df.csv')
col1, mid, col2 = st.columns([1, 3, 20])
with col1:
    st.image('public/logo.png', width=100)
with col2:
    st.markdown("""---""")
    st.markdown('###  Home Price Prediction')


with st.form("my_form"):
    st.markdown("# Prediction of Home Prices")

    date = st.date_input("Choose Date", dt.date(2000, 2, 1))

    new_construction = st.slider("New Constructions Parameter", min(df['new_construction'])-10, max(
        df['new_construction'])+50, 107.03)

    gdp = st.slider("GDP Parameter", min(
        df['gdp'])-10, max(df['gdp'])+10, 101.5)

    fed_rate = st.slider("Federal Rate Parameter", min(
        df['fed_rate']), max(df['fed_rate'])+0.1, 5.79)

    permit = st.slider("Number of Permits", min(
        df['permit'])-20, max(df['permit'])+20, 1692)

    mortgage_rate = st.slider("Mortgage Rate Parameter", min(
        df['mortgage_rate']), max(df['mortgage_rate']), 8.2)

    personal_income = st.slider("Person Income Parameter", min(
        df['personal_income']), max(df['personal_income']), 8400.00)

    submitted = st.form_submit_button("Submit")
    if submitted:
        date = dt.datetime.toordinal(date)
        model = pickle.load(open('reg.pkl', 'rb'))
        prediction = model.predict(
            [[date, new_construction, gdp, fed_rate, permit, mortgage_rate, personal_income]])
        st.write("Predicted Home Price:", prediction[0])
