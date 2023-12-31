# -*- coding: utf-8 -*-
"""Mega_Sena.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RfLliOtyW0317rtffPi28GjR3Js7we4W
"""

import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_excel('/content/Mega_sena.xlsx')

dados.head

colunas_bolas = ['bola 1', 'bola 2', 'bola 3', 'bola 4', 'bola 5', 'bola 6']

todos_numeros = dados[colunas_bolas].stack()

frequencia_numeros = todos_numeros.value_counts()

frequencia_numeros = frequencia_numeros.sort_index()

plt.bar(frequencia_numeros.index, frequencia_numeros.values)
plt.xlabel('Número Sorteado')
plt.ylabel('Frequência')
plt.title('Frequência dos Números Sorteados da Mega Sena')
plt.show()

for numero in range(1, 61):
    frequencia = frequencia_numeros.get(numero, 0)
    print(f'Número {numero}: {frequencia} vezes')

dados['Data'] = pd.to_datetime(dados['Data'], format='%d/%m/%Y')

dados['Ano'] = dados['Data'].dt.year

colunas_bolas = ['bola 1', 'bola 2', 'bola 3', 'bola 4', 'bola 5', 'bola 6']

frequencia_por_ano = {}

for ano in dados['Ano'].unique():
    dados_ano = dados[dados['Ano'] == ano]
    todos_numeros = dados_ano[colunas_bolas].stack()
    frequencia_numeros = todos_numeros.value_counts()
    frequencia_por_ano[ano] = frequencia_numeros

for ano, frequencia_numeros in frequencia_por_ano.items():
    print(f'Ano {ano}:')
    for numero in range(1, 61):
        frequencia = frequencia_numeros.get(numero, 0)
        print(f'  Número {numero}: {frequencia} vezes')

dados_ultimo_ano = dados[dados['Ano'] == 2023]

numeros_pares = dados_ultimo_ano[['bola 1', 'bola 2', 'bola 3', 'bola 4', 'bola 5', 'bola 6']].applymap(lambda x: x % 2 == 0)
frequencia_pares = numeros_pares.sum().sum()

frequencia_impares = len(dados_ultimo_ano) * 6 - frequencia_pares

# Imprimir os resultados
print(f'No último ano, números pares foram sorteados {frequencia_pares} vezes.')
print(f'No último ano, números ímpares foram sorteados {frequencia_impares} vezes.')

import pandas as pd
from datetime import datetime, timedelta

# Carregue os dados no Power BI (certifique-se de que você já possui os dados carregados)

# Defina a data de referência como o último dia do último mês
data_referencia = datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1)

# Filtrar os dados para o último mês
dados_ultimo_mes = dados[dados['Data'] >= data_referencia.replace(day=1)]
dados_ultimo_mes = dados_ultimo_mes[dados_ultimo_mes['Data'] <= data_referencia]

# Contar a frequência de números pares e ímpares em todos os concursos do último mês
numeros_pares = dados_ultimo_mes[['bola 1', 'bola 2', 'bola 3', 'bola 4', 'bola 5', 'bola 6']].applymap(lambda x: x % 2 == 0)
frequencia_pares = numeros_pares.sum().sum()

frequencia_impares = len(dados_ultimo_mes) * 6 - frequencia_pares

# Imprimir os resultados
print(f'No último mês, números pares foram sorteados {frequencia_pares} vezes.')
print(f'No último mês, números ímpares foram sorteados {frequencia_impares} vezes.')

import pandas as pd

# Carregue os dados no Power BI (certifique-se de que você já possui os dados carregados)

# Filtrar os dados para o último mês (como no código anterior)
# Defina a data de referência como o último dia do último mês
data_referencia = datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1)

dados_ultimo_mes = dados[dados['Data'] >= data_referencia.replace(day=1)]
dados_ultimo_mes = dados_ultimo_mes[dados_ultimo_mes['Data'] <= data_referencia]

# Combine as colunas das bolas em uma única série de dados
colunas_bolas = ['bola 1', 'bola 2', 'bola 3', 'bola 4', 'bola 5', 'bola 6']
todos_numeros = dados_ultimo_mes[colunas_bolas].stack()

# Calcule a frequência de cada número
frequencia_numeros = todos_numeros.value_counts()

# Separe os números em pares e ímpares
numeros_pares = frequencia_numeros[frequencia_numeros.index % 2 == 0]
numeros_impares = frequencia_numeros[frequencia_numeros.index % 2 != 0]

# Selecione os três números mais frequentes de cada grupo (par e ímpar)
tres_numeros_pares = numeros_pares.head(3).index.tolist()
tres_numeros_impares = numeros_impares.head(3).index.tolist()

# Imprima os resultados
print('Três números pares mais frequentes:', tres_numeros_pares)
print('Três números ímpares mais frequentes:', tres_numeros_impares)

import pandas as pd

# Carregue os dados no Power BI (certifique-se de que você já possui os dados carregados)

# Filtrar os dados para o último mês (como no código anterior)
# Defina a data de referência como o último dia do último mês
data_referencia = datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1)

dados_ultimo_mes = dados[dados['Data'] >= data_referencia.replace(day=1)]
dados_ultimo_mes = dados_ultimo_mes[dados_ultimo_mes['Data'] <= data_referencia]

# Combine as colunas das bolas em uma única série de dados
colunas_bolas = ['bola 1', 'bola 2', 'bola 3', 'bola 4', 'bola 5', 'bola 6']
todos_numeros = dados_ultimo_mes[colunas_bolas].stack()

# Calcule a frequência de cada número
frequencia_numeros = todos_numeros.value_counts()

# Separe os números em pares e ímpares
numeros_pares = frequencia_numeros[frequencia_numeros.index % 2 == 0]
numeros_impares = frequencia_numeros[frequencia_numeros.index % 2 != 0]

# Selecione os três números pares mais frequentes
tres_numeros_pares = numeros_pares.head(3).index.tolist()

# Selecione os três números ímpares mais frequentes
tres_numeros_impares = numeros_impares.head(3).index.tolist()

# Contagem da frequência de cada um dos seis números selecionados
frequencia_numeros_selecionados = {}
for numero in tres_numeros_pares + tres_numeros_impares:
    frequencia_numeros_selecionados[numero] = todos_numeros[todos_numeros == numero].count()

# Imprima a frequência de cada número selecionado
for numero, frequencia in frequencia_numeros_selecionados.items():
    print(f'Número {numero}: A cada {frequencia} concursos')

import pandas as pd
from datetime import datetime, timedelta

# Carregue os dados no Power BI (certifique-se de que você já possui os dados carregados)

# Filtrar os dados para o último mês (como no código anterior)
# Defina a data de referência como o último dia do último mês
data_referencia = datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0) - timedelta(days=1)

dados_ultimo_mes = dados[dados['Data'] >= data_referencia.replace(day=1)]
dados_ultimo_mes = dados_ultimo_mes[dados_ultimo_mes['Data'] <= data_referencia]

# Combine as colunas das bolas em uma única série de dados
colunas_bolas = ['bola 1', 'bola 2', 'bola 3', 'bola 4', 'bola 5', 'bola 6']
todos_numeros = dados_ultimo_mes[colunas_bolas].stack()

# Calcule a frequência de cada número de 01 a 60
frequencia_numeros = todos_numeros.value_counts().reindex(range(1, 61), fill_value=0)

# Imprima a frequência de cada número
for numero, frequencia in frequencia_numeros.items():
    print(f'Número {numero}: {frequencia} vezes')

import pandas as pd

# Carregue os dados no Power BI (certifique-se de que você já possui os dados carregados)

# Filtrar os dados para os últimos 10 concursos
dados_ultimos_10_concursos = dados.tail(10)

# Combine as colunas das bolas em uma única série de dados
colunas_bolas = ['bola 1', 'bola 2', 'bola 3', 'bola 4', 'bola 5', 'bola 6']
todos_numeros = dados_ultimos_10_concursos[colunas_bolas].stack()

# Calcule a frequência de cada número de 01 a 60
frequencia_numeros = todos_numeros.value_counts().reindex(range(1, 61), fill_value=0)

# Imprima a frequência de cada número
for numero, frequencia in frequencia_numeros.items():
    print(f'Número {numero}: {frequencia} vezes')

import pandas as pd

# Carregue os dados no Power BI (certifique-se de que você já possui os dados carregados)

# Filtrar os dados para os últimos 10 concursos
dados_ultimos_10_concursos = dados.tail(10)

# Combine as colunas das bolas em uma única série de dados
colunas_bolas = ['bola 1', 'bola 2', 'bola 3', 'bola 4', 'bola 5', 'bola 6']
todos_numeros = dados_ultimos_10_concursos[colunas_bolas].stack()

# Números que você deseja calcular a frequência
numeros_interesse = [6, 58, 44, 9, 13, 35]

# Calcule a frequência de cada número de interesse nos últimos 10 concursos
frequencia_numeros_interesse = todos_numeros[todos_numeros.isin(numeros_interesse)].value_counts()

# Crie um dicionário com frequência 0 para números que não apareceram
frequencia_com_zeros = {numero: frequencia_numeros_interesse.get(numero, 0) for numero in numeros_interesse}

# Imprima a frequência de cada número de interesse, incluindo zeros
for numero, frequencia in frequencia_com_zeros.items():
    print(f'Número {numero}: {frequencia} vezes')

import pandas as pd

# Carregue os dados no Power BI (certifique-se de que você já possui os dados carregados)

# Filtrar os dados para os últimos 05 concursos
dados_ultimos_05_concursos = dados.tail(5)

# Combine as colunas das bolas em uma única série de dados
colunas_bolas = ['bola 1', 'bola 2', 'bola 3', 'bola 4', 'bola 5', 'bola 6']
todos_numeros = dados_ultimos_05_concursos[colunas_bolas].stack()

# Números que você deseja calcular a frequência
numeros_interesse = [6, 58, 44, 9, 13, 35]

# Calcule a frequência de cada número de interesse nos últimos 10 concursos
frequencia_numeros_interesse = todos_numeros[todos_numeros.isin(numeros_interesse)].value_counts()

# Crie um dicionário com frequência 0 para números que não apareceram
frequencia_com_zeros = {numero: frequencia_numeros_interesse.get(numero, 0) for numero in numeros_interesse}

# Imprima a frequência de cada número de interesse, incluindo zeros
for numero, frequencia in frequencia_com_zeros.items():
    print(f'Número {numero}: {frequencia} vezes')

import pandas as pd
import matplotlib.pyplot as plt

# Carregue os dados no Power BI (certifique-se de que você já possui os dados carregados)

# Filtrar os dados para os últimos 10 concursos
dados_ultimos_10_concursos = dados.tail(10)

# Combine as colunas das bolas em uma única série de dados
colunas_bolas = ['bola 1', 'bola 2', 'bola 3', 'bola 4', 'bola 5', 'bola 6']
todos_numeros = dados_ultimos_10_concursos[colunas_bolas].stack()

# Calcule a frequência de cada número de 01 a 60
frequencia_numeros = todos_numeros.value_counts().reindex(range(1, 61), fill_value=0)

# Selecione os 10 números mais frequentes
top_10_numeros = frequencia_numeros.head(10)

# Crie um gráfico de barras
plt.bar(top_10_numeros.index, top_10_numeros.values)
plt.xlabel('Número Sorteado')
plt.ylabel('Frequência')
plt.title('Top 10 Números mais Frequentes nos Últimos 10 Concursos')
plt.xticks(rotation=45)
plt.show()



