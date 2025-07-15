import streamlit as st
from utils.db import get_strategies

data = get_strategies()

st.markdown(
    """
    <div style='text-align: center;'>
        <img src="./images/logo.png" style="width:150px; height:auto;" />
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("<h1 style='text-align: center;'>Strategies</h1>", unsafe_allow_html=True)
st.markdown("""
<p style='text-align: center;'>
  In the following section, you'll find an overview of the trading strategies currently active in the portfolio.<br>
  Each description offers a high-level summary, designed to convey the core concept without disclosing proprietary details.
</p>
""", unsafe_allow_html=True)

st.markdown("---")

for strategy in data:
    with st.container():
        st.markdown(f"**Strategy** {strategy['bot_id']}")
        st.markdown(f"{strategy['description']}")
        st.markdown("---")