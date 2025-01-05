import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def create_exploratory_visualizations():
    merged_data = pd.read_csv('data/merged/merged_data.csv')

    # Asigură-te că coloana 'Date' este de tip datetime
    merged_data['Date'] = pd.to_datetime(merged_data['Date'])

    # Adaugă o coloană 'Month' pentru a extrage luna din data fiecărei înregistrări
    merged_data['Month'] = merged_data['Date'].dt.month

    # Setează stilul pentru grafice
    sns.set(style="whitegrid")
    
    fig, axes = plt.subplots(3, 2, figsize=(15, 12))

    # 1. Histogramă pentru a vizualiza distribuția valorilor pentru o coloană numerică (ex. 'Close')
    sns.histplot(merged_data['Close'], kde=True, color='blue', ax=axes[0, 0])
    axes[0, 0].set_title('Distribuția Prețurilor de Închidere')

    # 2. Scatter plot pentru a vizualiza relația între două variabile (ex. 'Close' și 'Volume')
    sns.scatterplot(x=merged_data['Close'], y=merged_data['Volume'], color='green', ax=axes[0, 1])
    axes[0, 1].set_title('Preț de Închidere vs Volum')

    # 3. Heatmap pentru a vizualiza corelațiile dintre variabile
    correlation_matrix = merged_data.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', ax=axes[1, 0])
    axes[1, 0].set_title('Matricea de Corelație')

    # 4. Boxplot pentru a analiza distribuția și outlier-urile pentru variabila 'Close'
    sns.boxplot(x=merged_data['Close'], color='purple', ax=axes[1, 1])
    axes[1, 1].set_title('Distribuția Prețurilor de Închidere cu Boxplot')

    # 5. Time Series Plot pentru a vizualiza evoluția unei variabile (ex. 'Close') pe o perioadă de timp
    sns.lineplot(data=merged_data, x='Date', y='Close', marker='o', color='red', ax=axes[2, 0])
    axes[2, 0].set_title('Evoluția Prețului de Închidere în Timp')

    # 6. Violin plot pentru a vizualiza distribuția 'Close' în funcție de lună
    sns.violinplot(x='Month', y='Close', data=merged_data, ax=axes[2, 1], hue='Month', palette="muted", legend=False)
    axes[2, 1].set_title('Distribuția Prețului de Închidere pe Luni')

    # Ajustăm layout-ul
    fig.tight_layout()

    return fig
