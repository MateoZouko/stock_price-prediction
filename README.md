
# Stock Price Prediction

In this project I trained a Machine Learning model that is able to predict the price of the stock "Apple". During the develompent I load the stock data, preprocess it, engineer the features that I wanted to make the technical analysis, train the model and make the predictions. It also includes a chart that helps to visualize the prediction.

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

This task seeks to determine what the value of a company is from the data that is recorded on the stock exchange. A large body of information was analysed so as to help in the development of machine learning models through which specific parameters might be evaluated for stock valuation purposes which would enable one to accurately predict future values without any difficulty whatsoever. The outcomes comprised graphical explanations on market movements where they compared real-time prices with their earlier values that were projected into the future.

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

The training model uses features created from raw stock price, such as closing price, price difference, and moving average for prior training data. It trains the model by partitioning the data into two sets and estimates its accuracy using Mean Squared Error (MSE).

## Prediction

After training, the model makes predictions on the test set. These predictions are saved in `data/processed/predictions.csv`.

## Visualization

The project includes functionality to visualize the actual versus predicted stock prices. The plot is saved as `data/processed/stock_price_predictions.png`.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure your code follows the project’s coding standards.
