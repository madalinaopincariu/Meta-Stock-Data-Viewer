import pandas as pd

def merge_cleaned_data():
    # Căile fișierelor curățate
    cleaned_scraped_path = 'data/cleaned/scraped_data_cleaned.csv'  # Va fi al treilea în ordine cronologică
    cleaned_alpha_vantage_path = 'data/cleaned/alpha_vantage_data_cleaned.csv'  # Va fi primul în ordine cronologică
    cleaned_tabular_path = 'data/cleaned/tabular_data_cleaned.csv'  # Va fi al doilea în ordine cronologică
    
    # Fișierul de ieșire
    merged_output_path = 'data/merged/merged_data.csv'
    
    # Citirea fișierelor curățate
    scraped_data = pd.read_csv(cleaned_scraped_path)
    alpha_vantage_data = pd.read_csv(cleaned_alpha_vantage_path)
    tabular_data = pd.read_csv(cleaned_tabular_path)
    
    # Inversarea ordinii pentru al treilea fișier (scraped_data)
    scraped_data = scraped_data.sort_values(by='Date', ascending=False)
    
    # Inversarea ordinii pentru al doilea fișier (tabular_data)
    tabular_data = tabular_data.sort_values(by='Date', ascending=False)
    
    # Concatenarea datelor în ordinea dorită
    merged_data = pd.concat([alpha_vantage_data, tabular_data, scraped_data], ignore_index=True)
    
    # Asigurarea ordinii coloanelor
    merged_data = merged_data[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
    
    # Curățare:
    # Eliminarea liniilor duplicate
    merged_data = merged_data.drop_duplicates()
    
    # Eliminarea liniilor cu locuri goale (NaN)
    merged_data = merged_data.dropna()
    
    # Conversia coloanei 'Date' la tipul datetime pentru a te asigura că este corect
    merged_data['Date'] = pd.to_datetime(merged_data['Date'], errors='coerce')
    
    # Eliminarea liniilor cu date invalide
    merged_data = merged_data.dropna(subset=['Date'])
    
    # Resetarea indexului după curățare
    merged_data = merged_data.reset_index(drop=True)
    
    # Salvarea datelor îmbinate curățate
    merged_data.to_csv(merged_output_path, index=False)
    print(f"Fișierul îmbinat și curățat a fost salvat la: {merged_output_path}")
