import pandas as pd

def transform(data):
    data = pd.read_csv(data)
    data.dropna()

    return data