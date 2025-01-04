import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time
from datetime import datetime

def fetch_meta_stocks_raw(output_path: str):
    """
    Fetch historical stock data for Meta Platforms (META) from Yahoo Finance and saves it as a raw CSV file.

    :param output_path: Path to save the raw scraped data
    """
    url = "https://finance.yahoo.com/quote/META/history"
    
    # Define the start and end date for the data extraction (UNIX timestamps)
    end_date = int(time.time())  # Current time (present)
    start_date = int(time.mktime(datetime(2012, 1, 1).timetuple()))  # 1 January 2012

    params = {
        "period1": start_date,
        "period2": end_date,
        "interval": "1d",  # Daily data
        "filter": "history",
        "frequency": "1d",
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    print("Fetching raw data from Yahoo Finance...")
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Locate the historical prices table using the class name
    table = soup.find("table", class_="table yf-j5d1ld noDl")
    if not table:
        print("Failed to locate the historical prices table.")
        return

    # Extract rows from the table
    rows = table.find_all("tr")
    data = []

    for row in rows[1:]:
        cols = row.find_all("td")
        if len(cols) < 7:  # Skip rows without sufficient columns
            continue

        date = cols[0].text.strip()
        open_price = cols[1].text.strip().replace(',', '')
        high = cols[2].text.strip().replace(',', '')
        low = cols[3].text.strip().replace(',', '')
        close = cols[4].text.strip().replace(',', '')
        adj_close = cols[5].text.strip().replace(',', '')  # Adj Close column added
        volume = cols[6].text.strip().replace(',', '')

        # Append the data row
        data.append([date, open_price, high, low, close, adj_close, volume])

    # Convert to a DataFrame
    columns = ["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]
    df = pd.DataFrame(data, columns=columns)

    # Save the raw data to CSV
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Raw data saved to {output_path}")

def clean_meta_stocks_data(input_path: str, output_path: str):
    """
    Clean the raw Meta stock data and saves it as a cleaned CSV file.

    :param input_path: Path to the raw data CSV file
    :param output_path: Path to save the cleaned data
    """
    # Load the raw data from CSV
    df = pd.read_csv(input_path)

    # Clean the data
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date"])  # Remove rows with invalid dates
    df = df.astype({"Open": "float", "High": "float", "Low": "float", "Close": "float", "Adj Close": "float", "Volume": "float"})

    # Drop the 'Adj Close' column
    df = df.drop(columns=["Adj Close"])

    # Filter data for the years 2012, 2013, 2014, 2015
    df = df[df["Date"].dt.year.isin([2012, 2013, 2014, 2015])]

    # Replace missing values with 0 (if any)
    df.fillna(0, inplace=True)

    # Save the cleaned data to CSV
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")
