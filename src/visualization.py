import matplotlib.pyplot as plt

def plot_simples(df, coluna):
    df[coluna].plot(kind='hist')
    plt.title(f"Distribuição da coluna: {coluna}")
    plt.show()
