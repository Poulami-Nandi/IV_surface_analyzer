import matplotlib.pyplot as plt
import seaborn as sns

def plot_iv_vs_strike(df):
    plt.figure(figsize=(12, 6))
    for exp in df['expirationDate'].unique():
        subset = df[df['expirationDate'] == exp]
        plt.plot(subset['strike'], subset['impliedVolatility'], marker='o', label=str(exp.date()))
    plt.title("IV vs Strike")
    plt.xlabel("Strike Price")
    plt.ylabel("Implied Volatility")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_iv_heatmap(df, expiration):
    subset = df[df['expirationDate'].dt.date == expiration]
    pivot = subset.pivot_table(index='strike', columns='expirationDate', values='impliedVolatility')
    plt.figure(figsize=(8, 6))
    sns.heatmap(pivot, annot=True, fmt=".2f", cmap='YlGnBu')
    plt.title(f"IV Heatmap for {expiration}")
    plt.xlabel("Expiration Date")
    plt.ylabel("Strike Price")
    plt.tight_layout()
    plt.show()

def plot_iv_vs_expiry(df):
    plt.figure(figsize=(12, 6))
    top_strikes = sorted(df['strike'].unique())[:5]
    for strike in top_strikes:
        subset = df[df['strike'] == strike]
        plt.plot(subset['T'], subset['impliedVolatility'], marker='o', label=f'Strike {strike}')
    plt.xlabel("Time to Expiry (Years)")
    plt.ylabel("Implied Volatility")
    plt.title("IV vs Time to Expiry")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_iv_boxplot(df):
    df['exp_str'] = df['expirationDate'].dt.strftime('%Y-%m-%d')
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='exp_str', y='impliedVolatility', data=df)
    plt.xlabel("Expiration Date")
    plt.ylabel("Implied Volatility")
    plt.title("IV Distribution by Expiration")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
