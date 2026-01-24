import pandasimport pandas as pd

def write_online_store():
    df = pd.read_csv("data/features/features.csv")
    latest_df = df.tail(1)
    latest_df.to_csv("data/features/online_features.csv", index=False)
 as pd

def write_online_store():
    df = pd.read_csv("data/features/features.csv")
    latest_df = df.tail(1)
    latest_df.to_csv("data/features/online_features.csv", index=False)
