#!/usr/bin/env python
# coding: utf-8

# <center><b>UNIVERSIDADE FEDERAL RURAL DO SEMI-ÁRIDO</b> </center>
# <center><b>Inteligência Artificial</b></center>
# 
# 
# <h3><center>Implementação de algoritmos de aprendizado de máquina para análise de
# padrões em ações do mercado Financeiro</center></h3>
# 
# 
# <div style="text-align: right;">Anderson Carlos da Silva Morais</div>
# <div style="text-align: right;">Anderson Matheus Melo da Silva</div>
# 
# 
# 
# <center><b>Proposta</b></center>
# <b>Introdução:</b> Nos últimos anos, temos presenciado a popularização e disseminação da inteligência
# artificial e dos algoritmos de aprendizado de máquina em várias áreas. Um campo que tem se
# beneficiado dessas tecnologias é o mercado financeiro, onde o uso desses algoritmos para análise de
# ações tem se tornado uma prática comum. No entanto, é importante destacar que a promessa de
# retornos financeiros milagrosos e a venda de produtos e softwares enganosos têm gerado
# desconfiança nesse cenário.
# 
# <b>Objetivo:</b> O objetivo deste projeto é explorar o uso de algoritmos de aprendizado de máquina para
# análise de padrões no mercado financeiro de forma ética e didática. O projeto busca fornecer um
# ambiente de estudo no qual será possível entender e aplicar diferentes algoritmos de ML em um
# contexto real, utilizando um conjunto de dados definido de ações.
# Metodologia:
# 1. <b>Coleta de Dados:</b> Será realizado um levantamento de dados históricos de ações de
# empresas, utilizando fontes confiáveis e de acesso público. Os dados incluirão informações
# como preço de abertura, preço de fechamento, volume de negociação, entre outros
# indicadores relevantes.
# 2. <b>Pré-processamento dos Dados:</b> Os dados coletados passarão por um processo de limpeza e
# transformação, a fim de remover ruídos e garantir a qualidade dos dados. Serão aplicadas
# técnicas de normalização e tratamento de valores ausentes, quando necessário.
# 3. <b>Exploração de Algoritmos de Aprendizado de Máquina:</b> Serão utilizados diferentes
# algoritmos de aprendizado de máquina, como regressão linear, árvores de decisão, redes
# neurais, entre outros, para analisar os dados coletados. Cada algoritmo será aplicado e
# avaliado em termos de desempenho na identificação de padrões relevantes no mercado
# financeiro.
# 4. <b>Avaliação e Interpretação dos Resultados:</b> Os resultados obtidos serão analisados e
# interpretados de forma a identificar padrões e tendências no mercado financeiro. Serão
# realizadas métricas de desempenho para avaliar a eficácia dos algoritmos utilizados. É
# importante ressaltar que este projeto não tem como objetivo fornecer recomendações de
# compra ou venda de ações, mas sim estudar os conceitos de ML em um contexto real.
# 
# <b>Justificativa:</b> Este projeto visa explorar o uso de algoritmos de aprendizado de máquina para análise
# de padrões no mercado financeiro. A proposta é utilizar um conjunto de dados definido de ações
# para aplicar diferentes algoritmos e entender seu desempenho na identificação de padrões
# relevantes. Ao final do projeto, espera-se obter um maior entendimento sobre o uso de ML no
# mercado financeiro, contribuindo para o avanço do conhecimento nessa área.
# 
# <b>Observação:</b> É importante ressaltar que este projeto destina-se apenas ao estudo e compreensão dos
# conceitos de aprendizado de máquina em um contexto real. Não deve ser interpretado como
# recomendação de compra ou venda de ações. Sempre consulte profissionais especializados antes de
# tomar decisões financeiras.
# 
# 

# # Etapa 1: Coleta de Dados

# In[1]:


# Realizando as importações das bibliotecas necessárias
import pandas as pd # Para o tratamento de dados
import numpy as np # Para o tratamento de dados
import cfscrape # Para realizar a requisição na raspagem de dados
# from bs4 import BeautifulSoup as bs # Para auxiliar na raspagem de dados
import unidecode # Para o tratamento de Strings
import datetime # Para exportar os dados com a data da raspagem 


# A base de dados usada para o projeto é o site [Fundamentus](https://www.fundamentus.com.br/fii_resultado.php).

# In[2]:


# Usando a biblioteca cfscrape para obter uma requisição do site

# cabeçalhos para acessar
# headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}

# url do site
url = "https://www.fundamentus.com.br/fii_resultado.php"

# ferramenta de scrap para obter a requisição
scraper = cfscrape.create_scraper()
response = scraper.get(url)


# In[3]:


# Printando a resposta da requisição HTTP, caso 200 é que tudo deu certo
print(response)


# In[4]:


## Resíduo de análise antigas, não excluir! ##
# Acessando o conteúdo HTML da resposta da requisição com formatação html esparço, mais fácil de se trabalhar
# soup = bs(response.content, "html.parser")

# Para visualizar o HTML do site basta tirar o ; do recurso abaixo
# soup.content


# In[5]:


## Resíduo de análise antigas, não excluir! ##
# Filtrando o HTML para apenas a tabela de ações
# n = soup.find("table")


# In[6]:


## Resíduo de análise antigas, não excluir! ##
# type(n)


# In[7]:


# Lendo a tabela HTML como um dataframe do Pandas

# O código gera uma lista das tabelas encontradas no HTML, sendo as tabelas representadas como dataframes
# basta indicar o índice da tabela para acessá-la
dt= pd.read_html(response.content)[0]
dt

## Uma maneira alternativa de acessar a lista de dataframes ##

# gerando a lista de dataframes
# dt= pd.read_html(response.content)
# Acessando o dataframe
# dt[0]


# # Etapa 2: Pré-processamento dos Dados
# 
# Essa etapa é voltada ao tratamento dos dados obtidos da raspagem, pois durante o processo os dados sofreram alterações na sua tipagem, além de estarem em um formato que dificulte o trabalho dentro de um ambiente de programação.
# 
# Um cuidado que será tomado para evitar o tempo na coleta de dados caso os dados sofram uma formatação errada é de usar uma cópia do dataset Original nas formatações.

# In[8]:


# Criando um cópia do dataset original para o tratamento de dados
dt_test = dt.copy()


# In[9]:


# Observando as informações dos dados do Dataframe para identificar as limpezas necessárias
dt_test.info()


# In[10]:


# Visualizando o nome das colunas
dt_test.columns


# **Obs:** As colunas possuem nomes com caracteres inválidos e que dificultam o trabalho, sendo necessário modifica-las

# In[11]:


## Resíduo de análise antigas, não excluir! ##
# Salvando os antigos nomes das colunas para um possível uso futuro
# colunas_antigas = dt_test.columns

# Modificando os nomes das colunas para um padrão mais usual de se trabalhar
colunas = []
for nome in dt_test.columns:
    text = nome.strip().replace(' ','_').lower().replace('/','_sobre_') # múltiplos tratamentos de strings
    text = unidecode.unidecode(text) # removendo caracteres acentuados 
    colunas.append(text)
    
colunas


# In[12]:


# Atribuindo as novas colunas
dt_test.columns = colunas


# In[13]:


# Visualizando a modificação
dt_test.head(3)


# **Obs:** os dados numéricos estão usando o separador de casas decimais com vírgula, realizando o tratamento:

# In[14]:


# Removendo a pontuação dos dados no Dataset
# Os códigos a partir daqui devesse tomar cuidado para não rodar mais de uma vez, para evitar gerar erros.
dt_test = dt_test.apply(lambda x: x.str.replace(".",'', regex=True) if x.dtype=="object" else x)

## Resíduo de análise antigas, não excluir! ##
# Não funciona
# dt_test.replace(',','.', regex=True, inplace=True)


# In[15]:


# Visualizando o dataset para verificar se o tratamento foi aplicado
# Algumas colunas irão precisar de tratamento especiais, realizados mais na frente
dt_test


# **Obs:** modificando o separador decimal para o ponto:

# In[16]:


# Substituindo a vígula por ponto no dataset
dt_test.replace(',','.', regex=True, inplace=True)

## Resíduo de análise antigas, não excluir! ##
## Outra forma de fazer ##
#dt_test = dt_test.apply(lambda x: x.str.replace(",",".") if x.dtype=="object" else x)


# In[17]:


# Visualizando o dataset para verificar se o tratamento foi aplicado
dt_test


# In[18]:


# Visualizando os tipos das colunas para os próximos tratamentos
dt_test.info()


# **Obs:** Os tipos de cada colunas estão como texto, é necessário fazer a tipagem correta das colunas para o tipo numérico e deixar as colunas percentuais em um formato decimal. O caso das colunas especiais: **preco_do_m2, aluguel_por_m2, cotacao e segmento** será tratado mais adiante.

# In[19]:


# Colunas numéricas
colunas_numericas = ["p_sobre_vp",
                     "valor_de_mercado",
                     "liquidez",
                     "qtd_de_imoveis"]

for coluna in colunas_numericas:
    dt_test[coluna] = dt_test[coluna].astype(float) # Modificando o tipo da coluna

# Colunas percentuais
colunas_percentuais = ["ffo_yield",
                       "dividend_yield",
                       "cap_rate",
                       "vacancia_media"]

for coluna in colunas_percentuais:
    dt_test[coluna] = dt_test[coluna].str.replace("%","", regex=True).astype(float) # Removendo o % e transformando em tipo float
    dt_test[coluna] = dt_test[coluna].apply(lambda x: x/100) # passando a porcentagem para a forma decimal

# p_sobre_vp precisa do mesmo ajuste para o formato decimal
dt_test.p_sobre_vp = dt_test.p_sobre_vp.apply(lambda x: x/100) # passando a porcentagem para a forma decimal


# In[20]:


# Visualizando o dataset para verificar se o tratamento foi aplicado corretamente
dt_test


# In[21]:


# Visualizando os tipos de dados do dataset
dt_test.info()


# In[22]:


# Modificando uma configuração do pandas para melhorar a visualização de valores muito grandes
pd.set_option('display.float_format', '{:.2f}'.format)


# In[23]:


# Visualizando o dataset novamente
dt_test


# **Obs:** agora tratando os casos especiais, que são, para a coluna segmento a presença de valores do tipo NaN, que como estão em uma coluna textual serão substituidos pelo texto "Desconhecido". Já as colunas "preco_do_m2", "cotação" e "aluguel_por_m2" que exigem um tratamento especifíco para uma notação monetária com duas casas decimais.

# In[24]:


# Tratando os dados do tipo NaN para serem o texto "Desconhecido"
dt_test.segmento = dt_test.segmento.fillna('Desconhecido') 


# In[25]:


# Tratando a coluna de "preco_do_m2"
# Quando foi feita o tratamentos de dados anteriores alguns valores perderam seu separador decimal e outros não

# Removendo os pontos para um tratamento uniforme nos dados
dt_test.preco_do_m2 = dt_test.preco_do_m2.str.replace(".","", regex=True)

# Sabemos que todos os aluguéis possuem duas casas decimais e estão no mesmo padrão, podemos mover o separador em duas casas dividindo por 100
dt_test.preco_do_m2 = dt_test.preco_do_m2.astype(float).apply(lambda x: x/100) # Divindindo todos os valores por 100, garantido duas casas decimais e modificando para o tipo para numérico


# In[26]:


# Tratando a coluna de "aluguel_por_m2"
# Quando foi feita o tratamentos de dados anteriores alguns valores perderam seu separador decimal e outros não

# Removendo os pontos para um tratamento uniforme nos dados
dt_test.aluguel_por_m2 = dt_test.aluguel_por_m2.str.replace(".","", regex=True)

# Sabemos que todos os aluguéis possuem duas casas decimais e estão no mesmo padrão, podemos mover o separador em duas casas dividindo por 100
dt_test.aluguel_por_m2 = dt_test.aluguel_por_m2.astype(float).apply(lambda x: x/100) # Divindindo todos os valores por 100, garantido duas casas decimais e modificando para o tipo para numérico


# In[27]:


# Tratando a coluna de cotação
# Quando foi feita o tratamentos de dados anteriores alguns valores perderam seu separador decimal e outros não

# Removendo os pontos para um tratamento uniforme nos dados
dt_test.cotacao = dt_test.cotacao.str.replace(".","", regex=True)

# Sabemos que todos os preços possuem duas casas decimais e estão no mesmo padrão, podemos mover o separador em duas casas dividindo por 100
dt_test.cotacao = dt_test.cotacao.astype(float).apply(lambda x: x/100) # Divindindo todos os valores por 100, garantido duas casas decimais e modificando o tipo para numérico


# In[28]:


dt_test# Visualizando o dataset para verificar se o tratamento foi aplicado
dt_test.head(10)


# **Obs:** Como os dados variam diariamente, é interessante adicionar as datas de cada raspagem para diferenciar o conjunto de dados

# In[29]:


# Resgatando a data do sistema para exportar o arquivo com sua data respectiva de tratamento

dia_de_raspagem = datetime.datetime.now().date() # puxando as datas
dia_de_raspagem = dia_de_raspagem.strftime("_%d_%m_%Y") # definindo o formatado da data
dt_test.to_csv(f"planilhas_fundamentus_fii/teste{dia_de_raspagem}.csv", index=False) # exportando como arquivo csv


# # Etapa 3: Exploração de Algoritmos de Aprendizado de Máquina

# # Etapada 4: Avaliação e Interpretação dos Resultados

# In[ ]:




