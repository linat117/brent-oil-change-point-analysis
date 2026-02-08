import matplotlib.pyplot as plt
import pandas as pd


def plot_price_series(
    df: pd.DataFrame,
    date_col: str = "date",
    price_col: str = "price"
) -> None:
    """
    Plot Brent oil price time series.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing price data.
    """
    if date_col not in df.columns or price_col not in df.columns:
        raise ValueError(
            f"DataFrame must contain '{date_col}' and '{price_col}' columns"
        )

    try:
        plt.figure(figsize=(14, 5))
        plt.plot(df[date_col], df[price_col])
        plt.title("Brent Oil Price Over Time")
        plt.xlabel("Date")
        plt.ylabel("Price (USD)")
        plt.grid(True)
        plt.show()
    except Exception as e:
        print(f"Failed to generate plot: {e}")
