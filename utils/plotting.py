import plotly.express as px


def plot_equity(df):
    df = df.sort_values(by='timestamp')  # cambia con il tuo campo timestamp
    df['equity'] = df['profit'].cumsum()  # cambia con il tuo campo profit
    return px.line(df, x='timestamp', y='equity', title='Equity Line')
