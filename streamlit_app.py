import streamlit as st
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
from scipy.optimize import brentq

st.set_page_config(page_title="Implied Volatility Surface", layout="wide")

# ----------------------------
# Utility Functions
# ----------------------------

def black_scholes_price(S, K, T, r, sigma, option_type='call'):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if option_type == 'call':
        return S * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)
    else:
        return K * np.exp(-r*T) * norm.cdf(-d2) - S * norm.cdf(-d1)

def implied_volatility(market_price, S, K, T, r, option_type='call'):
    try:
        return brentq(lambda sigma: black_scholes_price(S, K, T, r, sigma, option_type) - market_price, 1e-5, 5.0)
    except:
        return np.nan

def get_option_chain(ticker, max_expirations=3):
    stock = yf.Ticker(ticker)
    expirations = stock.options[:max_expirations]
    all_options = []
    for date in expirations:
        chain = stock.option_chain(date)
        calls = chain.calls.copy()
        calls['expirationDate'] = date
        calls['optionType'] = 'call'
        puts = chain.puts.copy()
        puts['expirationDate'] = date
        puts['optionType'] = 'put'
        all_options.extend([calls, puts])
    df = pd.concat(all_options, axis=0)
    df.reset_index(drop=True, inplace=True)
    return df

def compute_iv(df, spot, r):
    df['expirationDate'] = pd.to_datetime(df['expirationDate'])
    df['T'] = (df['expirationDate'] - pd.Timestamp.today()).dt.days / 365.0
    df['mid'] = (df['bid'] + df['ask']) / 2
    df['impliedVolatility'] = df.apply(
        lambda row: implied_volatility(row['mid'], spot, row['strike'], row['T'], r, row['optionType'])
        if row['T'] > 0 and row['mid'] > 0 else np.nan,
        axis=1
    )
    return df

# ----------------------------
# Sidebar
# ----------------------------

st.sidebar.title("🔧 Options Settings")
ticker = st.sidebar.text_input("Stock Ticker", value="AAPL")
r = st.sidebar.slider("Risk-Free Rate", min_value=0.0, max_value=0.1, step=0.001, value=0.01)
option_type = st.sidebar.selectbox("Option Type", options=["call", "put"])
max_exp = st.sidebar.slider("Max Expiration Dates", min_value=1, max_value=10, value=3)

# ----------------------------
# Main Logic
# ----------------------------

if st.sidebar.button("Fetch and Analyze"):
    with st.spinner("Fetching data and computing implied volatilities..."):
        spot_price = yf.Ticker(ticker).history(period="1d")['Close'].iloc[-1]
        chain_df = get_option_chain(ticker, max_exp)
        iv_df = compute_iv(chain_df, spot_price, r)
        filtered = iv_df[(iv_df['optionType'] == option_type) & (iv_df['impliedVolatility'].notna())]

    st.success(f"Data fetched for {ticker}. Spot Price: {spot_price:.2f}")

    # Plot: IV vs Strike per Expiration
    st.subheader("📈 IV vs Strike for Different Expirations")
    fig1, ax1 = plt.subplots(figsize=(12, 6))
    for exp in filtered['expirationDate'].unique():
        subset = filtered[filtered['expirationDate'] == exp]
        ax1.plot(subset['strike'], subset['impliedVolatility'], marker='o', label=str(exp.date()))
    ax1.set_title("IV vs Strike")
    ax1.set_xlabel("Strike Price")
    ax1.set_ylabel("Implied Volatility")
    ax1.grid(True)
    ax1.legend()
    st.pyplot(fig1)

    # 🔥 Heatmap with reduced tick clutter
    selected_exp = st.selectbox("Select Expiration for Heatmap", options=filtered['expirationDate'].dt.date.unique())
    st.subheader(f"🔥 IV Heatmap for {selected_exp}")
    exp_filtered = filtered[filtered['expirationDate'].dt.date == selected_exp]

    if not exp_filtered.empty:
        heatmap_data = exp_filtered.pivot_table(
            index='expirationDate',
            columns='strike',
            values='impliedVolatility'
        )

        col1, col2, col3 = st.columns([0.1, 0.8, 0.1])
        with col2:
            fig2, ax2 = plt.subplots(figsize=(14, 4))
            sns.heatmap(
                heatmap_data,
                annot=False,
                fmt=".2f",
                cmap='YlGnBu',
                linewidths=0.3,
                cbar=True,
                ax=ax2
            )
            ax2.set_xlabel("Strike Price")
            ax2.set_ylabel("")
            ax2.set_title(f"Implied Volatility Heatmap - {selected_exp}")
            xticks = ax2.get_xticks()
            xticklabels = [label.get_text() for label in ax2.get_xticklabels()]
            # Reduce label clutter by only showing every 3rd label
            ax2.set_xticks(xticks[::3])
            ax2.set_xticklabels(xticklabels[::3], rotation=45)
            st.pyplot(fig2)
    else:
        st.warning("No data available for the selected expiration.")

    # Plot: IV vs Time to Expiry
    st.subheader("🕒 IV vs Time to Expiry for Selected Strikes")
    fig3, ax3 = plt.subplots(figsize=(12, 6))
    top_strikes = sorted(filtered['strike'].unique())[:5]
    for strike in top_strikes:
        subset = filtered[filtered['strike'] == strike]
        ax3.plot(subset['T'], subset['impliedVolatility'], marker='o', label=f'Strike {strike}')
    ax3.set_xlabel("Time to Expiry (Years)")
    ax3.set_ylabel("Implied Volatility")
    ax3.set_title("IV vs Time to Expiry")
    ax3.legend()
    ax3.grid(True)
    st.pyplot(fig3)

    # Plot: Boxplot
    st.subheader("📦 IV Distribution by Expiration")
    fig4, ax4 = plt.subplots(figsize=(12, 6))
    filtered['exp_str'] = filtered['expirationDate'].dt.strftime('%Y-%m-%d')
    sns.boxplot(x='exp_str', y='impliedVolatility', data=filtered, ax=ax4)
    ax4.set_xlabel("Expiration Date")
    ax4.set_ylabel("Implied Volatility")
    ax4.set_title("IV Boxplot")
    plt.xticks(rotation=45)
    st.pyplot(fig4)

else:
    st.info("👈 Enter a stock ticker and click 'Fetch and Analyze' to begin.")
