from typing import Optional
import pandas as pd


def load_brent_data(
    filepath: str,
    date_col: str = "date",
    price_col: str = "price"
) -> pd.DataFrame:
    """
    Load and clean Brent oil price data.

    Parameters
    ----------
    filepath : str
        Path to the CSV file.
    date_col : str
        Name of the date column.
    price_col : str
        Name of the price column.

    Returns
    -------
    pd.DataFrame
        Cleaned DataFrame with parsed dates, sorted by time.
    """
    try:
        df = pd.read_csv(filepath)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {filepath}")

    required_cols = {date_col, price_col}
    if not required_cols.issubset(df.columns):
        raise ValueError(f"CSV must contain columns: {required_cols}")

    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
    df = df.dropna(subset=[date_col, price_col])

    df = df.sort_values(by=date_col).reset_index(drop=True)

    return df
