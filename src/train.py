import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from .model import create_model


def train_model(df):
    """
    Train the machine learning model
    """
    X = df[['Prev Close']].values
    y = df['Close'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = create_model()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    print(f"Mean Squared Error: {mse}")

    return model

if __name__ == "__main__":
    df = pd.read_csv('../data/processed/processed_data_with_features.csv')
    model = train_model(df)