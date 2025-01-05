# src/clustering/clustering_model.py

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """Încarcă datele dintr-un fișier CSV."""
    return pd.read_csv(file_path)

def preprocess_data(data):
    """Preprocesează datele pentru clustering:
       - Normalizarea datelor.
    """
    # Alegem coloanele de interes (fără 'Date', care nu este numeric)
    columns_to_use = ['Open', 'High', 'Low', 'Close', 'Volume']
    
    # Standardizează datele
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data[columns_to_use])
    
    return scaled_data

def apply_kmeans_clustering(scaled_data, n_clusters=3):
    """Aplică algoritmul KMeans pentru clustering."""
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(scaled_data)
    
    # Adăugăm etichetele clusterelor în datele originale
    return kmeans.labels_

def visualize_clusters(data, labels):
    """Vizualizează rezultatele clusteringului."""
    # Adăugăm etichetele clusterelor în DataFrame-ul original
    data['Cluster'] = labels
    
    # Vizualizare folosind un scatter plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x='Open', y='Close', hue='Cluster', palette='viridis', s=100, alpha=0.7)
    plt.title('Vizualizare Clustere pe baza Prețului de Deschidere și Prețului de Închidere')
    plt.xlabel('Preț de Deschidere')
    plt.ylabel('Preț de Închidere')
    plt.legend(title='Cluster')
    plt.show()
