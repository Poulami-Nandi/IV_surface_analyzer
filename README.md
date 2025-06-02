
# 📊 Implied Volatility Surface Analyzer

![Streamlit App Screenshot](https://github.com/Poulami-Nandi/IV_surface_analyzer/raw/main/images/demo/banner_screenshot.png)

An interactive Streamlit dashboard to analyze and visualize **Implied Volatility (IV)** surfaces, volatility smiles, skews, and term structures for stock options using the **Black-Scholes model**.

---

## 🚀 Live App

▶️ [Launch the App](https://ivsurfaceanalyzer-fv9ni87dppyftsappw6q87h.streamlit.app)

---

## 🧠 Project Overview

This tool fetches **real-time options data** using `yfinance`, computes implied volatility using the **Black-Scholes formula**, and provides a suite of visualizations:

- 📈 IV vs Strike (Volatility smile/skew)
- 🧊 IV Heatmap for selected expiry
- 🕒 IV vs Time to Expiry
- 📦 IV Boxplot by Expiry
- ⚖️ IV vs Moneyness (S/K)
- 🎯 IV Scatter plot colored by time to expiry

---

## 🔧 Features

- Interactive sidebar controls for:
  - Stock ticker
  - Risk-free rate
  - Option type (call/put)
  - Number of expirations to analyze
- Real-time data fetching and preprocessing
- Robust handling of edge cases (e.g., zero bids/asks, invalid options)
- Built-in email and affiliation banner

---

## 📷 Banner & Author Info

<img src="https://github.com/Poulami-Nandi/IV_surface_analyzer/raw/main/images/own/own_image.jpg" alt="Profile" width="150"/>

**👩‍🔬 Dr. Poulami Nandi**  
Physicist · Quant Researcher · Data Scientist  
[University of Pennsylvania](https://live-sas-physics.pantheon.sas.upenn.edu/people/poulami-nandi) | [IIT Kanpur](https://www.iitk.ac.in/) | [TU Wien](http://www.itp.tuwien.ac.at/CPT/index.htm?date=201838&cats=xbrbknmztwd)

📧 [nandi.poulami91@gmail.com](mailto:nandi.poulami91@gmail.com), [pnandi@sas.upenn.edu](mailto:pnandi@sas.upenn.edu)  
🔗 [LinkedIn](https://www.linkedin.com/in/poulami-nandi-a8a12917b/) • [GitHub](https://github.com/Poulami-Nandi) • [Google Scholar](https://scholar.google.co.in/citations?user=bOYJeAYAAAAJ&hl=en)

---

## 📁 Project Structure

```
IV_surface_analyzer/
├── streamlit_app.py             # Streamlit application
├── utils/
│   ├── bs_model.py
│   ├── fetch_data.py
│   ├── visualizations.py
├── requirements.txt             # Python dependencies
├── images/
│   ├── demo/                    # Screenshots from streamlit app
│   ├── own/                     # Author image
│   └── AAPL/                    # AAPL-specific plots
└── README.md                    # Project documentation
```

---

## 📦 Installation

To run locally:

```bash
git clone https://github.com/Poulami-Nandi/IV_surface_analyzer.git
cd IV_surface_analyzer
pip install -r requirements.txt
streamlit run streamlit_app.py
```

---

## 📈 Sample Visuals

### IV vs Strike (Volatility Smile)

![IV vs Strike](https://github.com/Poulami-Nandi/IV_surface_analyzer/raw/main/images/AAPL/IVvsStrikeAAPL.png)

### IV Heatmap for Selected Expiry

![IV Heatmap](https://github.com/Poulami-Nandi/IV_surface_analyzer/raw/main/images/AAPL/IVheatmapAAPL.png)

### IV vs Time to Expiry

![IV vs Time to Expiry](https://github.com/Poulami-Nandi/IV_surface_analyzer/raw/main/images/AAPL/IVdistributionAAPL.png)

### IV Boxplot by Expiry

![IV Boxplot](https://github.com/Poulami-Nandi/IV_surface_analyzer/raw/main/images/AAPL/IVvsTimeAAPL.png)

### IV vs Moneyness (S/K)

![IV vs Moneyness](https://github.com/Poulami-Nandi/IV_surface_analyzer/raw/main/images/AAPL/IVvsMoneynessAAPL.png)

### IV Scatter Plot Colored by Time to Expiry

![IV Scatter Plot](https://github.com/Poulami-Nandi/IV_surface_analyzer/raw/main/images/AAPL/IVvsStrikeWithTimeToExpiryAAPL.png)

---

## 📐 Mathematical Foundations

### Black-Scholes Model for Option Pricing

The Black-Scholes formula is used to price European-style options and forms the basis for implied volatility calculation.

For a **call option**, the Black-Scholes price `C` is:

```
C = S * N(d1) - X * exp(-r * T) * N(d2)
```

For a **put option**:

```
P = X * exp(-r * T) * N(-d2) - S * N(-d1)
```

Where:
- `S`: Current price of the underlying asset
- `X`: Strike price of the option
- `T`: Time to maturity (in years)
- `r`: Risk-free interest rate
- `N(.)`: Cumulative distribution function of the standard normal distribution

The terms `d1` and `d2` are:

```
d1 = [ ln(S/X) + (r + σ²/2) * T ] / (σ * sqrt(T))
d2 = d1 - σ * sqrt(T)
```

---

### Implied Volatility via Brent’s Method

Implied volatility `σ_impl` is the value of `σ` such that:

```
Observed_Price = BlackScholes(S, X, T, r, σ_impl)
```

We solve this using the **Brent root-finding method** to find the volatility that equates theoretical and observed prices.

---

### Vega (Sensitivity to Volatility)

```
Vega = S * sqrt(T) * N'(d1)
```

Where `N'(d1)` is the standard normal PDF. Vega shows how much the option price changes with volatility.

---

## 💡 Future Work

- Add Vega/Delta/Gamma analytics
- SVI surface fitting
- Historical IV backtesting
- Option strategy P&L visualizer

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

Thanks to:

- [yfinance](https://github.com/ranaroussi/yfinance)
- [Streamlit](https://streamlit.io/)
- [SciPy](https://scipy.org/)
