# src/data_loader.py

import pandas as pd  # Biblioteca usada para ler e manipular dados tabulares

# Função para carregar o dataset CSV
def load_data(filepath: str) -> pd.DataFrame:
    """
    Carrega um arquivo CSV usando pandas.

    Parâmetros:
    - filepath (str): Caminho até o arquivo CSV

    Retorno:
    - pd.DataFrame: Dados carregados em forma de tabela (linhas e colunas)
    """
    df = pd.read_csv(filepath)  # Lê o CSV e converte para DataFrame
    return df  # Retorna os dados para quem chamou a função
