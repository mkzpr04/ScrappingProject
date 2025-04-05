import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

#Create the dash app
app = dash.Dash(__name__)

#Defining the layout of the dashboard
app.layout = html.Div([
     html.H1("Crypto Dashboard"),
     dcc.Graph(id='price-graph'),
     #Update every 5 minutes
     dcc.Interval(id='interval-component',interval=5*60*1000, n_intervals=0),
     html.H2("Daily Report"),
     html.Div(id ='daily-report')
])

@app.callback(
     Output('price-graph','figure'),
     [Input('interval-component', 'n_intervals')]

)
def update_graph(n):
    df = pd.read_csv('crypto_data.csv')
    print("DEBUG: df;head() =>")
    print(df.head())
    fig = px.line(df, x='timestamp', y='price_btc', title='Bitcoin Price Over Time')
    return fig

@app.callback(
         Output('daily-report', 'children'),
         [Input('interval-component', 'n_intervals')]
)
def update_daily_report(n):
    return "Daily metrics will appear here (Volatility, open/close prices...)"

if __name__=='__main__':
   app.run(debug=True)
