import tkinter as tk
from tkinter import ttk
import pandas as pd
from PIL import Image, ImageTk
import os
from tkinter import PhotoImage
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from src.visualizations.data_analysis import create_exploratory_visualizations
from tkinter import Toplevel


# Funcții pentru a citi datele
def load_yahoo_data():
    try:
        df = pd.read_csv('data/cleaned/scraped_data_cleaned.csv')
        data_display.delete(1.0, tk.END)  # Curăță zona de text
        data_display.insert(tk.END, df.to_string())  # Afișează toate datele din dataframe
    except Exception as e:
        data_display.delete(1.0, tk.END)
        data_display.insert(tk.END, f"Error loading Yahoo data: {e}")

def load_alpha_vantage_data():
    try:
        df = pd.read_csv('data/cleaned/alpha_vantage_data_cleaned.csv')
        data_display.delete(1.0, tk.END)
        data_display.insert(tk.END, df.to_string())
    except Exception as e:
        data_display.delete(1.0, tk.END)
        data_display.insert(tk.END, f"Error loading Alpha Vantage data: {e}")

def load_tabular_data():
    try:
        df = pd.read_csv('data/cleaned/tabular_data_cleaned.csv')
        data_display.delete(1.0, tk.END)
        data_display.insert(tk.END, df.to_string())
    except Exception as e:
        data_display.delete(1.0, tk.END)
        data_display.insert(tk.END, f"Error loading Tabular data: {e}")

# Funcții pentru a citi datele raw
def load_yahoo_raw_data():
    try:
        df = pd.read_csv('data/raw/scraped_data.csv')
        data_display.delete(1.0, tk.END)
        data_display.insert(tk.END, df.to_string())  # Afișează datele raw
    except Exception as e:
        data_display.delete(1.0, tk.END)
        data_display.insert(tk.END, f"Error loading raw Yahoo data: {e}")

def load_alpha_vantage_raw_data():
    try:
        df = pd.read_csv('data/raw/alpha_vantage_data.csv')
        data_display.delete(1.0, tk.END)
        data_display.insert(tk.END, df.to_string())
    except Exception as e:
        data_display.delete(1.0, tk.END)
        data_display.insert(tk.END, f"Error loading raw Alpha Vantage data: {e}")

def load_tabular_raw_data():
    try:
        df = pd.read_csv('data/raw/tabular_data.csv')
        data_display.delete(1.0, tk.END)
        data_display.insert(tk.END, df.to_string())
    except Exception as e:
        data_display.delete(1.0, tk.END)
        data_display.insert(tk.END, f"Error loading raw Tabular data: {e}")

# Funcție pentru a curăța zona de text când schimbăm tab-ul
def clear_data_display(event):
    data_display.delete(1.0, tk.END)

# Funcție pentru a deschide o fereastră separată cu vizualizările exploratorii
def open_exploratory_visualizations():
    # Creăm o fereastră de top-level (nouă fereastră)
    visualizations_window = Toplevel()
    visualizations_window.title("Exploratory Visualizations")

    # Obținem vizualizările exploratorii
    fig = create_exploratory_visualizations()
    if fig:
        canvas = FigureCanvasTkAgg(fig, master=visualizations_window)  # Creează canvas-ul cu figura
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)  # Adaugă canvas-ul în fereastră

# Funcție pentru rularea clusteringului și salvarea rezultatelor
def run_clustering():
    try:
        from src.clustering.clustering_model import load_data, preprocess_data, apply_kmeans_clustering
        
        # Încarcă datele
        file_path = 'data/merged/merged_data.csv'
        data = load_data(file_path)
        
        # Preprocesează datele
        scaled_data = preprocess_data(data)
        
        # Aplică clustering
        labels = apply_kmeans_clustering(scaled_data, n_clusters=3)
        
        # Adaugă etichetele clusterelor în DataFrame
        data['Cluster'] = labels
        
        # Salvează datele cu clusterele într-un fișier nou
        output_path = 'data/merged/clustered_data.csv'
        data.to_csv(output_path, index=False)
        
        data_display.delete(1.0, tk.END)
        data_display.insert(tk.END, f"Clustering completed! Results saved to {output_path}\n")
        data_display.insert(tk.END, data.to_string())
    except Exception as e:
        data_display.delete(1.0, tk.END)
        data_display.insert(tk.END, f"Error running clustering: {e}")

# Funcție pentru a vizualiza clusteringul
def visualize_clustering():
    try:
        from src.clustering.clustering_model import visualize_clusters, load_data
        
        # Încarcă datele
        file_path = 'data/merged/clustered_data.csv'
        data = load_data(file_path)
        
        # Creează vizualizarea
        visualize_clusters(data, data['Cluster'])
    except Exception as e:
        data_display.delete(1.0, tk.END)
        data_display.insert(tk.END, f"Error visualizing clustering: {e}")

# Adăugarea funcționalității în tab-ul de clustering
def create_clustering_tab(notebook):
    tab_clustering = ttk.Frame(notebook)
    notebook.add(tab_clustering, text="Clustering")
    
    # Buton pentru a rula clusteringul
    run_clustering_button = ttk.Button(tab_clustering, text="Run Clustering", command=run_clustering)
    run_clustering_button.grid(row=0, column=0, padx=5, pady=5)
    
    # Buton pentru a vizualiza clusteringul
    visualize_clustering_button = ttk.Button(tab_clustering, text="Visualize Clustering", command=visualize_clustering)
    visualize_clustering_button.grid(row=0, column=1, padx=5, pady=5)
    
    return tab_clustering

# Creare fereastră principală
def create_ui():
    root = tk.Tk()
    root.title("Meta Stock Data Viewer")

    # Creare tab-uri
    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    # Tab pentru Yahoo Finance
    tab_yahoo = ttk.Frame(notebook)
    notebook.add(tab_yahoo, text="Yahoo Finance")

    yahoo_button = ttk.Button(tab_yahoo, text="Load Yahoo Finance Data", command=load_yahoo_data)
    yahoo_button.grid(row=0, column=0, padx=5, pady=5)
    yahoo_label = ttk.Label(tab_yahoo, text="Yahoo Finance Data")
    yahoo_label.grid(row=1, column=0, padx=5, pady=5)

    # Buton pentru încărcarea datelor raw pentru Yahoo
    yahoo_raw_button = ttk.Button(tab_yahoo, text="Load Raw Yahoo Data", command=load_yahoo_raw_data)
    yahoo_raw_button.grid(row=0, column=1, padx=5, pady=5)

    # Tab pentru Alpha Vantage
    tab_alpha_vantage = ttk.Frame(notebook)
    notebook.add(tab_alpha_vantage, text="Alpha Vantage")

    alpha_vantage_button = ttk.Button(tab_alpha_vantage, text="Load Alpha Vantage Data", command=load_alpha_vantage_data)
    alpha_vantage_button.grid(row=0, column=0, padx=5, pady=5)
    alpha_vantage_label = ttk.Label(tab_alpha_vantage, text="Alpha Vantage Data")
    alpha_vantage_label.grid(row=1, column=0, padx=5, pady=5)

    # Buton pentru încărcarea datelor raw pentru Alpha Vantage
    alpha_vantage_raw_button = ttk.Button(tab_alpha_vantage, text="Load Raw Alpha Vantage Data", command=load_alpha_vantage_raw_data)
    alpha_vantage_raw_button.grid(row=0, column=1, padx=5, pady=5)

    # Tab pentru Tabular Data
    tab_tabular = ttk.Frame(notebook)
    notebook.add(tab_tabular, text="Tabular Data")

    tabular_button = ttk.Button(tab_tabular, text="Load Tabular Data", command=load_tabular_data)
    tabular_button.grid(row=0, column=0, padx=5, pady=5)
    tabular_label = ttk.Label(tab_tabular, text="Tabular Data")
    tabular_label.grid(row=1, column=0, padx=5, pady=5)

    # Buton pentru încărcarea datelor raw pentru Tabular Data
    tabular_raw_button = ttk.Button(tab_tabular, text="Load Raw Tabular Data", command=load_tabular_raw_data)
    tabular_raw_button.grid(row=0, column=1, padx=5, pady=5)

    # Tab pentru Exploratory Visualizations
    exploratory_tab = ttk.Frame(notebook)  # Definirea tab-ului exploratoriu
    notebook.add(exploratory_tab, text="Exploratory Visualizations")
    
    # Buton pentru a deschide vizualizările exploratorii într-o fereastră separată
    exploratory_button = ttk.Button(exploratory_tab, text="Show Exploratory Visualizations", command=open_exploratory_visualizations)
    exploratory_button.pack(pady=5)

    create_clustering_tab(notebook)

    # Zona de afișare a datelor
    global data_display
    data_display = tk.Text(root, width=80, height=20, wrap=tk.WORD)
    data_display.pack(padx=10, pady=10)

    # Legăm funcția care curăță zona de text când schimbăm tab-ul
    notebook.bind("<<NotebookTabChanged>>", clear_data_display)

    return root