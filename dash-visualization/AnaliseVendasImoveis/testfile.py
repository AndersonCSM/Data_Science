import os
import plotly.express as px

# Obtém o diretório do script atual e constrói o caminho absoluto para o arquivo de chave
current_dir = os.path.dirname(__file__)
mapbox_key_path = os.path.join(current_dir, "keys/mapbox_key")

try:
    with open(mapbox_key_path, "r") as file:
        mapbox_access_token = file.read().strip()
        print("achou")
except FileNotFoundError:
    print(f"Erro: o arquivo '{mapbox_key_path}' não foi encontrado. Verifique o caminho e tente novamente.")
