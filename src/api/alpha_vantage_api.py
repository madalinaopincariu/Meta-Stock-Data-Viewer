import requests
import pandas as pd

def fetch_alpha_vantage_data(api_key: str, symbol: str, output_path: str):
    """
    Fetches stock data for a given symbol from Alpha Vantage API and saves it as a CSV file.

    :param api_key: Alpha Vantage API key
    :param symbol: Stock symbol (e.g., 'META' for Meta Platforms)
    :param output_path: Path to save the fetched data as a CSV file
    """
    url = "https://www.alphavantage.co/query"
    
    # Define the parameters for the API request
    params = {
        "function": "TIME_SERIES_DAILY",  # Function for daily time series
        "symbol": symbol,                 # Stock symbol (e.g., 'META')
        "apikey": api_key,                # Your Alpha Vantage API key
        "outputsize": "full",             # Full historical data
        "datatype": "csv",                # Return data in CSV format
    }
    
    # Make the request to the API
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Save the data to a CSV file
        with open(output_path, 'w') as f:
            f.write(response.text)
        print(f"Data saved to {output_path}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        print(f"Error message: {response.text}")

def clean_data(input_path: str, output_path: str):
    """
    Cleans the stock data by removing empty rows, ensuring proper formatting, and filtering by year.

    :param input_path: Path to the CSV file with raw data.
    :param output_path: Path to save the cleaned data.
    """
    # Read the CSV file
    df = pd.read_csv(input_path)

    # Drop any rows where all columns are NaN (empty rows)
    df.dropna(how="all", inplace=True)

    # Drop any rows where the 'timestamp' column (or equivalent) is NaN
    df.dropna(subset=['timestamp'], inplace=True)

    # Rename the 'timestamp' column to 'Date' (if applicable)
    if 'timestamp' in df.columns:
        df.rename(columns={'timestamp': 'Date', 'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close', 'volume': 'Volume'}, inplace=True)

    # Convert 'Date' to a datetime format
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Filter for the years 2021, 2022, 2023, 2024, 2025
    df = df[df['Date'].dt.year.isin([2021, 2022, 2023, 2024, 2025])]

    # Optionally, reset index after cleaning
    df.reset_index(drop=True, inplace=True)

    # Save the cleaned data to a new CSV file
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")