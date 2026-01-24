import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

def train():
    df = pd.read_csv("data/sample/features.csv")

    X = df[["avg_value", "tx_count"]]
    y = df["target"]

    model = LinearRegression()
    model.fit(X, y)

    joblib.dump(model, "data/sample/model.pkl")

if __name__ == "__main__":
    train()
