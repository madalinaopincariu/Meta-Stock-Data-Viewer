from src.scraping.scraper import fetch_meta_stocks_raw, clean_meta_stocks_data
from src.api.alpha_vantage_api import fetch_alpha_vantage_data, clean_data
from src.preprocessing.tabular_data_processing import clean_tabular_data
from ui.data_viewer import create_ui

def main():
    # Scrape raw data from Yahoo Finance (datele necurătate vor fi salvate în raw)
    scraped_data_raw_path = 'data/raw/scraped_data.csv'  # Fișierul cu datele necurățate
    fetch_meta_stocks_raw(scraped_data_raw_path)  # Datele necurățate din Yahoo Finance

    # Preprocess the scraped data (datele curățate vor fi salvate în cleaned)
    cleaned_scraped_output_path = 'data/cleaned/scraped_data_cleaned.csv'  # Fișierul cu datele curățate din web scraping
    clean_meta_stocks_data(scraped_data_raw_path, cleaned_scraped_output_path)  # Curățarea datelor extrase din Yahoo Finance

    # Fetching data from Alpha Vantage (datele necurățate vor fi salvate în raw)
    api_key = '2H6XU22QMNF0Z5IP'  # Înlocuiește cu cheia ta de API
    symbol = 'META'  # Stock symbol pentru Meta Platforms
    raw_output_path = 'data/raw/alpha_vantage_data.csv'  # Fișierul cu datele necurățate
    fetch_alpha_vantage_data(api_key, symbol, raw_output_path)  # Datele necurățate din Alpha Vantage

    # Clean the Alpha Vantage data (datele curățate vor fi salvate în cleaned)
    cleaned_output_path = 'data/cleaned/alpha_vantage_data_cleaned.csv'  # Fișierul cu datele curățate
    clean_data(raw_output_path, cleaned_output_path)  # Curățarea datelor din Alpha Vantage

    # Clean the tabular data (datele tabulare curățate vor fi salvate în cleaned)
    tabular_data_raw_path = 'data/raw/tabular_data.csv'  # Fișierul cu datele tabulare necurățate
    tabular_data_cleaned_path = 'data/cleaned/tabular_data_cleaned.csv'  # Fișierul cu datele tabulare curățate
    clean_tabular_data(tabular_data_raw_path, tabular_data_cleaned_path)  # Curățarea datelor tabulare

if __name__ == "__main__":
    app = create_ui()
    app.mainloop()