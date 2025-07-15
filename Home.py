from utils.plotting import plot_equity
from utils.db import get_balance
import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")

st.image("logo.png", use_container_width=False)

st.title("Trading Bot Dashboard!")

data = get_balance()

if data:
    df = pd.DataFrame(data)
    plot_equity(df)
else:
    st.warning("Nessun dato disponibile per il grafico di equity.")
