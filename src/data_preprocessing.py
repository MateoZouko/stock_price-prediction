import pandas as pd

def load_data(filepath):
    """Load raw data from a CSV file."""
    try:
        df = pd.read_csv(filepath)
        if df.empty:
            raise ValueError("No data found in the CSV file.")
        print(f"Data loaded successfully with {df.shape[0]} rows and {df.shape[1]} columns")
        return df
    except FileNotFoundError:
        print(f"Error: The file at {filepath} was not found.")
        raise
    except pd.errors.EmptyDataError:
        print("Error: No columns to parse from file. The file might be empty.")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

def preprocess_data(df):
    """Preprocess the raw data."""
    df['Prev Close'] = df['Close'].shift(1)
    df.dropna(inplace=True)
    print(f"Data after preprocessing: {df.shape[0]} rows and {df.shape[1]} columns")
    return df

if __name__ == '__main__':
    data = load_data('../data/raw/stock_data.csv')
    df = preprocess_data(df)
    df.to_csv('../data/processed/processed_data.csv', index=False)