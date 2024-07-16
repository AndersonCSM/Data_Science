from dash import html, dcc
import dash_bootstrap_components as dbc
from app import app

list_locations = {"All": 0, "Manhattan": 1, "Bronx": 2, "Brooklyn": 3, "Queens": 4, "Staten Island": 5}
slider_size = [100, 500, 1000, 10000, 10000000]

use_controllers = dbc.Row(
    [
        html.Img(
            id="capa",
            src=app.get_asset_url("Capa.png"),
            className="img-style",
        ),
        html.H3("Vendas de Imóveis - NYC", style={"margin-top": "30px"}),
        html.P(
            """Utilize o dashboard para analisar as vendas ocorridas na cidade de New York no período de 1 ano. """,
            style={"text-align": "justify"},
        ),
        #
        html.H4("""Distritos""", style={"margin-top": "50px", "margin-bottom": "20px"}),
        dcc.Dropdown(
            id="location-dropdown",
            options=[{"label": i, "value": j} for i, j in list_locations.items()],
            value=0,
            placeholder="Selecione um Destrito",
        ),
        #
        html.H4("""Metragem (m²)""", className="html-H4"),
        dcc.Slider(
            min=0,
            max=4,
            step=1,
            id="slider-square-size",
            marks={i: str(j) for i, j in enumerate(slider_size)},
        ),
        #
        html.H4("""Variável de Controle""", style={"margin-bottom": "20px", "margin-top": "20px"}),
        dcc.Dropdown(
            options=[
                {"label": "Ano de construção", "value": "YEAR BUILT"},
                {"label": "Total de unidades", "value": "TOTAL UNITS"},
                {"label": "Preço de venda", "value": "SALE PRICE"},
            ],
            value="SALE PRICE",
            id="dropdown-color",
        ),
        #
    ]
)
