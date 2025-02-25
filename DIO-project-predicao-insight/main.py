"""
Projeto para predição e insight de dados para o desafio do bootcamp de google AWS Sagemaker

A abordagem com python foi usada porque o Sagemaker é uma ferramenta da AWS que possui modelo
de precifição distinto e como forma de evitar eventuais pagamentos indevidos a abordagem de
código é a mais adequada, além de se tratar de um desafio simples.

Para a conclusão do projeto será usado jupyter-notebooks e principalmente o uso da biblioteca scikit-learn

Passo a passo do projeto
1 - Importa dados: url do github

2 - Enriquecimento de dados: limpeza, tratamento, separação

3 - Análise exploratória dos dados

3 - Treinamento do modelo de predição:
    Quantile Regression: É um método específico para estimar diferentes quantis da distribuição condicional de uma variável
    dependente. Você pode usar modelos como regressão quantílica para predizer diretamente os percentis desejados.
    
    Random Forest Quantile Regression: Uma extensão do algoritmo Random Forest que pode ser treinado para predizer quantis
    específicos da distribuição.
    
    Gradient Boosting Quantile Regression: Algoritmos como XGBoost ou LightGBM podem ser configurados para realizar regressão 
    quantílica, permitindo a predição de valores em diferentes percentis.
    
    Redes Neurais para Quantis: Redes neurais podem ser treinadas usando técnicas como regressão condicional ou diretamente
    para estimar quantis específicos da distribuição.

4 - Avaliação do modelo: uso em percentis por produtos únicos(10, 50 e 90 percentil)

5 - visualização aprimorada: dash com plotly
"""
