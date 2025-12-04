from sklearn.cluster import KMeans

def clusterizar(df, k):
    modelo = KMeans(n_clusters=k, random_state=42)
    modelo.fit(df)
    return modelo.labels_
