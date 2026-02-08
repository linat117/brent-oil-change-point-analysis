import pandas as pd


def load_brent_data(filepath: str) -> pd.DataFrame:
    """
    Load and clean Brent oil price data.
    """
    df = pd.read_csv(filepath)

    # Standardize column names
    df.columns = df.columns.str.lower()

    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date').reset_index(drop=True)

    return df
