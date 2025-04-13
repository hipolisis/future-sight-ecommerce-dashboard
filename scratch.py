import streamlit as st
import pandas as pd

@st.cache_data(ttl=300)  # Refresh every 5 minutes
def get_data():
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT4mRpLwHCmzA4-QiAOzFRk7GzeFC6Q6xu1cs4bL21KtzhIGjYofff2t8n2tOs6XYSAc3jdCOJcgpB7/pub?output=csv"
    return pd.read_csv(url, parse_dates=['timestamp'])  # Adjust column names

df = get_data()
st.dataframe(df)
print(df)