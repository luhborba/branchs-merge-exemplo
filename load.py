import pandas as pd

def load(path):
    data = pd.read_csv(path)
    data.to_parquet("data.parquet")