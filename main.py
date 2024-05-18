from src.data_preprocessing import load_data, preprocess_data
from src.feature_engineering import create_features
from src.train import train_model
from src.predict import predict
import pandas as pd

def main():
    # Load and preprocess data
    df = load_data('data/raw/stock_data.csv')
    df = preprocess_data(df)
    print(f"Data shape after loading and preprocessing: {df.shape}")

    # Save processed data
    df.to_csv('data/processed/processed_data.csv', index=False)
    
    # Create features
    df = create_features(df)
    print(f"Data shape after feature engineering: {df.shape}")

    # Save processed data with features
    df.to_csv('data/processed/processed_data_with_features.csv', index=False)
    
    # Check if DataFrame is empty before training
    if df.empty:
        print("Error: No data available for training after feature engineering.")
        return

    # Train model
    model = train_model(df)
    
    # Make predictions
    X = df[['Prev Close']].values
    predictions = predict(model, X)
    
    # Save predictions
    df['Predictions'] = predictions
    df.to_csv('data/processed/predictions.csv', index=False)
    print(df.head())

if __name__ == "__main__":
    main()
