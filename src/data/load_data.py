import pandas as pd

def load_brent_data(filepath: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")

    required_cols = {'date', 'price'}
    if not required_cols.issubset(df.columns.str.lower()):
        raise ValueError("CSV must contain 'date' and 'price' columns")

    df.columns = df.columns.str.lower()
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['date', 'price'])

    return df.sort_values('date').reset_index(drop=True)
