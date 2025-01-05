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

def load_clustered_data():
    try:
        # Încarcă fișierul cu rezultatele clustering-ului
        df = pd.read_csv('data/merged/merged_data.csv')
        data_display.delete(1.0, tk.END)  # Curăță zona de text
        data_display.insert(tk.END, df.to_string())  # Afișează toate datele din dataframe
    except Exception as e:
        data_display.delete(1.0, tk.END)
        data_display.insert(tk.END, f"Error loading clustered data: {e}")

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

    # Tab pentru Clustering
    tab_clustering = ttk.Frame(notebook)  # Creăm un tab pentru clustering
    notebook.add(tab_clustering, text="Clustering")

    # Buton pentru încărcarea datelor clustering
    clustering_button = ttk.Button(tab_clustering, text="Load Clustering Data", command=load_clustered_data)
    clustering_button.grid(row=0, column=0, padx=5, pady=5)

    # Zona de afișare a datelor
    global data_display
    data_display = tk.Text(root, width=80, height=20, wrap=tk.WORD)
    data_display.pack(padx=10, pady=10)

    # Legăm funcția care curăță zona de text când schimbăm tab-ul
    notebook.bind("<<NotebookTabChanged>>", clear_data_display)

    return root