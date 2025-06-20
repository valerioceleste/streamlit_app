import streamlit as st
from utils.db import get_transactions

st.title("Trade History")

df = get_transactions()
st.dataframe(df)
