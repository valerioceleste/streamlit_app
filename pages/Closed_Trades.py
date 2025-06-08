import streamlit as st
from utils.db import get_closed_trades

st.title("Closed Trades")

df = get_closed_trades()
st.dataframe(df)
