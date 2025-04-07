import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import os
from datetime import datetime

# Chemin absolu vers le dossier du script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Chemin vers le fichier CSV (conservé comme dans le premier code)
CSV_BTC = os.path.join(BASE_DIR, "crypto_data.csv")

# Création de l'application avec le thème Bootstrap LUX
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
app.title = "Crypto Dashboard"

# Layout modernisé comme dans le deuxième code
app.layout = dbc.Container([
    dbc.Row(
        dbc.Col(html.H1("Bitcoin Price Dashboard", className="text-center mb-4"), width=12)
    ),
    dbc.Row([
        dbc.Col(dcc.Graph(id='btc-graph'), width=12)  # Pleine largeur pour le graphique
    ]),
    dbc.Row([
        dbc.Col(dcc.Interval(
            id='interval-component',
            interval=5*60*1000,  # Mise à jour toutes les 5 minutes
            n_intervals=0
        ), width=12)
    ]),
    dbc.Row(
        dbc.Col(html.H2("Daily Report", className="mt-4 text-center"), width=12)
    ),
    dbc.Row(
        dbc.Col(html.Div(
            id='daily-report',
            style={
                "textAlign": "center",
                "fontSize": "18px",
                "backgroundColor": "#222",
                "color": "white",
                "padding": "10px",
                "borderRadius": "5px"
            }
        ), width=12)
    )
], fluid=True)

# Callback pour le graphique Bitcoin (même source de données que le premier code)
@app.callback(
    Output('btc-graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_btc_graph(n):
    try:
        df = pd.read_csv(CSV_BTC)
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
        df['price_btc'] = pd.to_numeric(df['price_btc'], errors='coerce')
        
        fig = px.line(
            df, 
            x='timestamp', 
            y='price_btc', 
            title="Bitcoin Price Over Time",
            labels={'price_btc': 'Price (USD)', 'timestamp': 'Date'}
        )
        fig.update_layout(
            template="plotly_dark",
            xaxis_title="Date",
            yaxis_title="Price (USD)",
            hovermode="x unified"
        )
        return fig
        
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return px.line(title="Error loading Bitcoin data")

# Callback pour le rapport journalier (version améliorée)
@app.callback(
    Output('daily-report', 'children'),
    [Input('interval-component', 'n_intervals')]
)
def update_daily_report(n):
    try:
        df = pd.read_csv(CSV_BTC)
        if len(df) > 0:
            latest = df.iloc[-1]
            report = f"""
            Latest Update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            Current BTC Price: ${latest['price_btc']:,.2f}
            24h High: ${df['price_btc'].max():,.2f}
            24h Low: ${df['price_btc'].min():,.2f}
            """
            return html.Pre(report)
        else:
            return "No data available"
    except Exception as e:
        print(f"Error generating report: {e}")
        return "Could not generate daily report"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8050)
