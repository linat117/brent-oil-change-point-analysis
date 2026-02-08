from typing import Optional
import pandas as pd
import matplotlib.pyplot as plt

def plot_series(
    df: pd.DataFrame,
    x_col: str,
    y_col: str,
    title: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    figsize: tuple[int, int] = (14, 5)
) -> None:
    """
    Plot a time series from a DataFrame.

    Parameters
    ----------
    df : pd.DataFrame
        Data containing x and y values.
    x_col : str
        Name of column for x-axis.
    y_col : str
        Name of column for y-axis.
    title : str, optional
        Plot title.
    xlabel : str, optional
        Label for x-axis.
    ylabel : str, optional
        Label for y-axis.
    figsize : tuple[int,int]
        Figure size.
    """
    if x_col not in df.columns or y_col not in df.columns:
        raise KeyError(f"Columns '{x_col}' and '{y_col}' must exist in DataFrame")

    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(df[x_col], df[y_col])
    ax.set_title(title or f"{y_col} vs {x_col}")
    ax.set_xlabel(xlabel or x_col)
    ax.set_ylabel(ylabel or y_col)
    ax.grid(True)
    plt.show()
