import pandas as pd

def carregar_csv(caminho):
    return pd.read_csv(caminho)

def resumo_df(df):
    print("Formato:", df.shape)
    print("Colunas:", df.columns)
    print(df.info())
