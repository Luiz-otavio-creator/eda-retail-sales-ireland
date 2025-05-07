# src/preprocess.py

import pandas as pd  # Biblioteca para manipulação de dados

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpa e transforma o DataFrame para análise exploratória.

    Parâmetros:
    df (pd.DataFrame): DataFrame original carregado do CSV.

    Retorna:
    pd.DataFrame: DataFrame processado e limpo.
    """

    # ================================
    # 1. Renomeando colunas para nomes mais descritivos
    # ================================
    df.columns = [
        'statistic_code',
        'statistic_label',
        'month_id',
        'month',
        'indicator_code',
        'sector',
        'unit',
        'value'
    ]

    # ================================
    # 2. Convertendo a coluna 'month' para o tipo datetime
    # ================================
    df['month'] = pd.to_datetime(df['month'], format='%Y %B')

    # ================================
    # 3. Ordenando os dados pela data
    # ================================
    df = df.sort_values('month')

    # ================================
    # 4. Removendo colunas que não serão usadas
    # ================================
    df = df.drop(columns=['statistic_code', 'statistic_label', 'month_id', 'indicator_code'])

    # ================================
    # 5. Resetando o índice (depois da ordenação)
    # ================================
    df = df.reset_index(drop=True)

    # ================================
    # 6. Verificando e removendo duplicatas, se houver
    # ================================
    df = df.drop_duplicates()

    return df  # Retorna os dados prontos para análise
