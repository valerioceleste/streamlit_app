import streamlit as st
from utils.db import get_open_trades

st.title("Open Trades")

df = get_open_trades()
st.dataframe(df)
