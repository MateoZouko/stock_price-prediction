import pandas as pd
from .model import create_model

def predict(model, X):
    """
    Make predictions using the trained model
    """
    return model.predict(X)

if __name__ == "__main__":
    df = pd.read_csv('../data/processed/processed_data_with_features.csv')
    X = df[['Prev Close']].values

    model = create_model()
    model.fit(X, df['Close'].values)

    predictions = predict(model, X)
    df['Predictions'] = predictions
    df.to_csv('../data/processed/predictions.csv', index=False)
    print(df.head())
