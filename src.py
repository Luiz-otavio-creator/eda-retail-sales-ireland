# src.py

# Importando bibliotecas para manipulação de caminhos e carregamento de dados
import os
from src.data_loader import load_data  # Importa a função que criamos
from src.preprocess import  preprocess_data #Funcao para limpar/preparar os dados
from src.visualization import (
    plot_sales_over_time,
    plot_seasonality_by_month,
    plot_top_sectors
)

# Descobrindo o caminho absoluto do diretório atual (onde está o src.py)
base_dir = os.path.dirname(os.path.abspath(__file__))


# Montando o caminho completo até o arquivo CSV
file_path = os.path.join(base_dir, 'data', 'raw', 'retail_sales_ireland.csv')

# Carregando os dados
df = load_data(file_path)

# Aplicando o pre-processamento nos dados Brutos
df_clean = preprocess_data(df)
'''
# Mostrando as 5 primeiras linhas da tabela
print("# Primeiras linhas do DataFrame")
print(df.head())

# Mostrando estrutura do DataFrame (colunas, tipos e nulos)
print("\n# Informações gerais sobre o DataFrame")
print(df.info())
'''
# Mostrando as primeiras linhas dos dados ja trabalhados
print("#Dados apos pre-processamento:")
print(df_clean.head())

# Mostra a estrutura geral dos dados limpos
print("\n# Infomacoes dos dados limpos:")
print(df_clean.info())

# Visualizacoes dos graficos
plot_sales_over_time(df_clean)
plot_seasonality_by_month(df_clean)
plot_top_sectors(df_clean, top_n=7)