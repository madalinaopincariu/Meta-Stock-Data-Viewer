import pandas as pd
import matplotlib.pyplot as plt

# Funcția de generare a vizualizărilor
def create_visualizations(data_path):
    # Încarcă datele procesate
    df = pd.read_csv(data_path)

    # Crează un plot pentru prețurile de închidere
    plt.figure(figsize=(10,6))
    plt.plot(df['Date'], df['Close'], label='Close Price', color='blue')
    plt.title('Meta (Facebook) Stock Close Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Close Price ($)')
    plt.grid(True)
    plt.legend()
    plt.show()

# Calea către datele procesate
data_path = '../data/processed/cleaned_data.csv'
create_visualizations(data_path)
