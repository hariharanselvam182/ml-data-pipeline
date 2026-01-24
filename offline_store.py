import pandas as pd
from datetime import datetime

def write_offline_store():
    df = pd.read_csv("data/features/features.csv")
    df["event_timestamp"] = datetime.now()
    df.to_csv("data/features/offline_features.csv", index=False)
