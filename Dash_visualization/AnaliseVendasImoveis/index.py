from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd


from app import app

from components._map import *
from components._histogram import *
from components._controllers import *

# ==============
# Data ingestion
# ==============
dataset = pd.read_csv(
    "https://github.com/AndersonCSM/Database/raw/main/Dash_visualizations/VendasImoveis/cleaned_data.csv", index_col=0
)

# Média de latitude e longitude
mean_lat = dataset["LATITUDE"].mean()
mean_long = dataset["LONGITUDE"].mean()

# Conversão de área
dataset["size_m2"] = dataset["GROSS SQUARE FEET"] / 10.764

# Filtragem de anos
dataset = dataset[dataset["YEAR BUILT"] > 0]

# Convertendo data
dataset["SALE DATE"] = pd.to_datetime(dataset["SALE DATE"])

# Padronizando magnitude de dados para uso
dataset.loc[dataset["size_m2"] > 10000, "size_m2"] = 10000
dataset.loc[dataset["SALE PRICE"] > 50000000, "SALE PRICE"] = 50000000
dataset.loc[dataset["SALE PRICE"] < 100000, "SALE PRICE"] = 100000

# ==============
# Layout
# ==============
app.layout = dbc.Container(
    children=[
        dbc.Row(
            [
                dbc.Col([], md=3),
                dbc.Col([map_fig, hist_fig], md=9),
            ]
        )
    ],
    fluid=True,
)


if __name__ == "__main__":
    app.run_server(debug=True)
    # app.run_server(host="0.0.0.0", port="8050")
