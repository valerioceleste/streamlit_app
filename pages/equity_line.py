import streamlit as st
from utils.db import get_closed_trades
from utils.plotting import plot_equity

st.title("Equity Line")

df = get_closed_trades()
fig = plot_equity(df)

st.plotly_chart(fig)
