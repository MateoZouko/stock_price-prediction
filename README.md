
# Stock Price Prediction

This project aims to predict stock prices using machine learning. It involves loading stock data, preprocessing it, engineering features, training a model, and making predictions. The project also includes a visualization of the actual versus predicted stock prices.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [Model Training](#model-training)
- [Prediction](#prediction)
- [Visualization](#visualization)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project predicts stock prices for a given company using historical stock data. The machine learning model is trained on various features engineered from the raw stock data. The results include a visualization comparing actual and predicted stock prices.

## Project Structure

```
root/
├── data/
│   ├── raw/
│   │   └── stock_data.csv
│   ├── processed/
│   │   └── processed_data.csv
│   │   └── predictions.csv
│   │   └── stock_price_predictions.png
├── src/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── train.py
│   └── predict.py
├── main.py
├── visualize.py
├── README.md
```

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/stock_price_prediction.git
    cd stock_price_prediction
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Data Preparation

1. Place your raw stock data file (`stock_data.csv`) in the `data/raw/` directory.

### Run the Main Script

1. Execute the main script to preprocess data, train the model, and make predictions:
    ```bash
    python3 main.py
    ```

### Visualize the Predictions

1. If you want to visualize the predictions separately, run the `visualize.py` script:
    ```bash
    python3 visualize.py
    ```

## Data

The project uses historical stock data which includes columns such as `Date`, `Open`, `High`, `Low`, `Close`, `Adj Close`, and `Volume`. Ensure your data is formatted correctly and placed in `data/raw/stock_data.csv`.

## Model Training

The model is trained using features engineered from the raw stock data, including previous closing price, price difference and moving average. The training process splits the data into training and testing sets and evaluates the model using Mean Squared Error (MSE).

## Prediction

After training, the model makes predictions on the test set. These predictions are saved in `data/processed/predictions.csv`.

## Visualization

The project includes functionality to visualize the actual versus predicted stock prices. The plot is saved as `data/processed/stock_price_predictions.png`.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure your code follows the project’s coding standards and includes appropriate tests.
