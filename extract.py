import pandas as pd

def extract():
    df = pd.read_csv('data.csv')
    df.to_csv('data.csv', index=False)
    