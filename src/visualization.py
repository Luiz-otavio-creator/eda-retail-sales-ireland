# src/visualization.py

import matplotlib.pyplot as plt #Graficos estaticos
import seaborn as sns # Graficos estaticos mais bonitos
import pandas as pd

# Configuracoes visuais padrao
sns.set(style= 'whitegrid')

def plot_sales_over_time(df: pd.DataFrame):
    '''
    Plots the overall trend of retail sales over time.
    Gera um grafico de linha mostrando a evolucao e evolucao das vendas ao longo do tempo
    '''

    plt.figure(figsize = (14,6)) #Tammanho do grafico
    sns.lineplot(data = df, x="month", y= "value")
    plt.title('Retail Sales trend Over Time in Ireland')
    plt.xlabel('Date')
    plt.ylabel('Retail Sales Index (Base 2015 = 100)')
    plt.tight_layout()
    plt.savefig("reports/trend.png", dpi=300)
    plt.show()
    input("Press Enter to continue...")

def plot_seasonality_by_month(df: pd.DataFrame):
    """
    Plots seasonal patterns by month using a boxplot.
    Gera um boxplot para mostrar a variação sazonal mês a mês.
    """
    df['month_number'] = df['month'].dt.month
    df['month_name'] = df['month'].dt.strftime('%b')

    plt.figure(figsize=(12, 6))
    order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
             'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(data=df, x='month_name', y='value', order=order)
    plt.title("Seasonality of Retail Sales by Month")
    plt.xlabel("Month")
    plt.ylabel("Retail Sales Index")
    plt.tight_layout()
    plt.savefig("reports/seasonality.png", dpi=300)
    plt.show()
    input("Press Enter to continue...")

def plot_top_sectors(df: pd.DataFrame, top_n=5):
    """
    Plots the top sectors with the highest average sales index.
    Mostra os setores com maior média de vendas.
    """
    plt.figure(figsize=(12, 6))
    sector_mean = df.groupby('sector')['value'].mean().sort_values(ascending=False).head(top_n)
    sns.barplot(x=sector_mean.values, y=sector_mean.index)
    plt.title(f"Top {top_n} Sectors by Average Retail Sales Index")
    plt.xlabel("Average Index")
    plt.ylabel("Sector")
    plt.tight_layout()
    plt.show()
    plt.savefig("reports/top_sectors.png", dpi=300)
    plt.show()
    input("Press Enter to continue...")
