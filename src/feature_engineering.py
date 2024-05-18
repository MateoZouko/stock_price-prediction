import pandas as pd

def create_features(df):
    """Create features for the model."""
    # Example feature: 5-day moving average
    df['Moving Average'] = df['Close'].rolling(window=2).mean()
    # Drop rows with NaN values after creating features
    df.dropna(inplace=True)
    print(f"Data after feature engineering: {df.shape[0]} rows and {df.shape[1]} columns")
    return df

if __name__ == "__main__":
    df = pd.read_csv('../data/processed/processed_data.csv')
    df = create_features(df)
    df.to_csv('../data/processed/processed_data_with_features.csv', index=False)
