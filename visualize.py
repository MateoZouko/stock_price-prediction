import pandas as pd
import matplotlib.pyplot as plt


def plot_predictions(df, save_path='data/processed/stock_price_predictions.png'):
    plt.figure(figsize=(14, 7))
    plt.plot(df['Date'], df['Close'], label='Actual Prices')
    plt.plot(df['Date'], df['Predictions'], label='Predicted Prices')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Stock Price Prediction')
    plt.legend()
    plt.savefig(save_path)  
    plt.close() 

if __name__ == "__main__":
    df = pd.read_csv('data/processed/predictions.csv')
    plot_predictions(df)
