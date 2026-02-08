import matplotlib.pyplot as plt


def plot_price_series(df):
    plt.figure(figsize=(14, 6))
    plt.plot(df['date'], df['price'])
    plt.title("Brent Oil Prices Over Time")
    plt.xlabel("Date")
    plt.ylabel("Price (USD per barrel)")
    plt.grid(True)
    plt.show()
