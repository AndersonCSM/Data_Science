import os
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np

import plotly.express as px

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
                dbc.Col([use_controllers], md=3),
                dbc.Col([map_fig, hist_fig], md=9),
            ]
        )
    ],
    fluid=True,
)


# ==============
# Callbacks
# ==============
@app.callback(
    # output
    [
        Output("hist-graph", "figure"),
        Output("map-graph", "figure"),
    ],
    # input
    [
        Input("location-dropdown", "value"),
        Input("slider-square-size", "value"),
        Input("dropdown-color", "value"),
    ],
)
def update_graphs(location, square_size, color_map):
    """
    TIP: poderia ser criados duas funções, uma para o histogram e outra para o gráfico,
    contudo, como os tratamentos aplicados são pertinentes para ambas as visualizações,
    ambas as visualizações serão trabalhadas em conjunto.
    """
    # Tratando problema caso não seja passado nenhum valor
    if location is None:
        df_intermediate = dataset.copy()  # Apenas a copia dos dados
    else:
        # os dados da localização escolhida, se a escolha for diferente de 0 (todos)
        # caso seja 0 (todos) apenas copie o dataset
        df_intermediate = dataset[dataset["BOROUGH"] == location] if location != 0 else dataset.copy()

        # definindo o tamanho limite de area escolhido, se a escolha não for None
        # se a escolhe for None, então retorne o tamanho limite máximo
        size_limit = slider_size[square_size] if square_size is not None else dataset["GROSS SQUARE FEET"].max()

        # Filtra o dataframe de acordo com o limite
        df_intermediate = df_intermediate[df_intermediate["GROSS SQUARE FEET"] <= size_limit]

    # Cria o histogram
    hist_fig = px.histogram(df_intermediate, x=color_map, opacity=0.75)

    # Cria o layout do histogram
    hist_layout = go.Layout(
        xaxis_title=color_map,
        yaxis_title='COUNT',
        margin=go.layout.Margin(l=10, r=0, t=0, b=50),
        showlegend=False,
        template="plotly_dark",
        paper_bgcolor="rgba(0, 0, 0, 0)",
    )
    hist_fig.layout = hist_layout

    KEY_PATH = get_path("keys/mapbox_key")
    px.set_mapbox_access_token(open(KEY_PATH).read())

    # Os dados não estão uniformemente distribuidos, é necessário realizar um processo para melhorar a visualização
    # Vamos separar os dados em percentis
    colors_rgb = px.colors.sequential.GnBu
    dt_quantiles = (
        dataset[color_map].quantile(np.linspace(0, 1, len(colors_rgb))).to_frame()
    )  # dados igualmente espaçados
    dt_quantiles = (dt_quantiles - dt_quantiles.min()) / (
        dt_quantiles.max() - dt_quantiles.min()
    )  # normalizando os dados (subtraindo pelo minimo e dividindo pelo máximo)
    dt_quantiles["colors"] = colors_rgb  # coluna de cores rgb para associar os percentis - valores - cores
    dt_quantiles.set_index(color_map, inplace=True)

    color_scale = [[i, j] for i, j in dt_quantiles["colors"].items()]  # escala de cores lineares

    map_fig = px.scatter_mapbox(
        df_intermediate,
        lat="LATITUDE",
        lon="LONGITUDE",
        color=color_map,
        size="size_m2",
        size_max=15,
        zoom=10,
        opacity=0.4,
    )
    map_fig.update_layout(
        mapbox=dict(center=go.layout.mapbox.Center(lat=mean_lat, lon=mean_long)),
        template="plotly_dark",
        paper_bgcolor="rgba(0, 0, 0, 0)",
        margin=go.layout.Margin(l=10, r=10, t=10, b=10),
    )
    map_fig.update_coloraxes(colorscale=color_scale)  # atualizando a escala de cores do gráfico

    return hist_fig, map_fig


def get_path(project_path):
    # Obtém o diretório do script atual e constrói o caminho absoluto para o arquivo de chave
    current_dir = os.path.dirname(__file__)
    path = os.path.join(current_dir, project_path)

    return path


if __name__ == "__main__":
    app.run_server(debug=True)
    # app.run_server(host="0.0.0.0", port="8050")
