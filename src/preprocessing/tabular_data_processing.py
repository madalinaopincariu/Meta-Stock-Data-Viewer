import pandas as pd
import os

def clean_tabular_data(input_path: str, output_path: str):
    """
    Curăță datele din fișierul CSV specificat și le salvează într-un fișier nou.

    :param input_path: Calea către fișierul CSV de intrare.
    :param output_path: Calea către fișierul CSV de ieșire.
    """
    # Citește fișierul CSV
    try:
        df = pd.read_csv(input_path)
        print(f"File '{input_path}' loaded successfully.")
    except Exception as e:
        print(f"Failed to load file: {e}")
        return

    # Verifică dacă fișierul conține date
    if df.empty:
        print("The dataset is empty.")
        return

    # Curățarea datelor:
    # 1. Elimină valorile lipsă
    # 2. Conversia tipurilor de date (dacă este cazul)
    
    # Verifică valorile lipsă
    print("\nCheck for missing values before cleaning:")
    print(df.isnull().sum())

    # Elimină rândurile cu valori lipsă, dacă sunt critice pentru analiza ta
    df = df.dropna(subset=['Date', 'Open', 'Close', 'High', 'Low', 'Volume']) 

    # Dacă sunt valori lipsă care nu afectează analiza, poți să le înlocuiești cu un alt valor (ex: 0)
    df.fillna(0, inplace=True)

    # Conversie la tipuri corespunzătoare (exemplu pentru prețuri și volume)
    df["Open"] = pd.to_numeric(df["Open"], errors="coerce")
    df["High"] = pd.to_numeric(df["High"], errors="coerce")
    df["Low"] = pd.to_numeric(df["Low"], errors="coerce")
    df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
    df["Volume"] = pd.to_numeric(df["Volume"], errors="coerce")

    # Conversia coloanei 'Date' într-un format datetime
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Dacă ai date invalide, le poți elimina
    df = df.dropna(subset=["Date"])

    # Filtrare pentru anii 2016, 2017, 2018, 2019, 2020
    df = df[df["Date"].dt.year.isin([2016, 2017, 2018, 2019, 2020])]

    # Elimină coloana 'Adj Close'
    df = df.drop(columns=["Adj Close"])

    # Verifică din nou valorile lipsă după curățare
    print("\nCheck for missing values after cleaning:")
    print(df.isnull().sum())

    # Verifică dacă DataFrame-ul mai conține date
    if df.empty:
        print("DataFrame is empty after cleaning.")
        return

    # Asigură-te că directorul de ieșire există
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Salvează fișierul curățat
    try:
        df.to_csv(output_path, index=False)
        print(f"Cleaned data saved to {output_path}")
    except Exception as e:
        print(f"Failed to save the cleaned data: {e}")