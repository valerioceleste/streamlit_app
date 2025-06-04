from utils.db import get_closed_trades
import streamlit as st


st.title("Trading Bot Dashboard !")

trades = get_closed_trades()
st.write("Numero di trade chiusi:", len(trades))
st.dataframe(trades)
