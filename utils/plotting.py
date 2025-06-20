import pandas as pd
import plotly.graph_objects as go
import streamlit as st


def plot_equity(df):
    # Converti timestamp in datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Calcola equity
    df['equity'] = df['free_capital'] + df['position_value']
    df['equity_unr'] = df['free_capital'] + \
        df['position_value'] + df['unrealized']

    # Ordina per timestamp
    df = df.sort_values('timestamp')

    # Crea grafico con Plotly
    fig = go.Figure()

    # Equity line (nera)
    fig.add_trace(go.Scatter(
        x=df['timestamp'],
        y=df['equity'],
        mode='lines+markers',
        name='Equity',
        line=dict(color='black', width=2),
        marker=dict(size=6)
    ))

    # Equity con unrealized (blu)
    fig.add_trace(go.Scatter(
        x=df['timestamp'],
        y=df['equity_unr'],
        mode='lines+markers',
        name='Equity (Unrealized)',
        line=dict(color='royalblue', width=2),
        marker=dict(size=6)
    ))

    fig.update_layout(
        title='Equity Over Time',
        xaxis_title='Timestamp',
        yaxis_title='Equity (USDT)',
        template='plotly_white',
        hovermode='x unified',
        yaxis=dict(range=[0, None])
    )

    st.plotly_chart(fig, use_container_width=True)
