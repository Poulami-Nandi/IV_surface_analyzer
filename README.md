
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

## 🧠 Mathematical Foundations

### Black-Scholes Model for Option Pricing

The Black-Scholes formula is used to price European-style options and forms the basis for implied volatility calculation. For a call option, the Black-Scholes price \( C \) is given by:

\[
C = S_0 \cdot N(d_1) - X \cdot e^{-rT} \cdot N(d_2)
\]

where:

- \( S_0 \): Current price of the underlying asset
- \( X \): Strike price of the option
- \( T \): Time to maturity of the option (in years)
- \( r \): Risk-free interest rate
- \( N(\cdot) \): Cumulative distribution function of the standard normal distribution

The terms \( d_1 \) and \( d_2 \) are calculated as:

\[
d_1 = rac{\ln\left(rac{S_0}{X}
ight) + \left(r + rac{\sigma^2}{2}
ight)T}{\sigma \sqrt{T}}, \quad d_2 = d_1 - \sigma \sqrt{T}
\]

For put options:

\[
P = X \cdot e^{-rT} \cdot N(-d_2) - S_0 \cdot N(-d_1)
\]

---

### Implied Volatility via Brent’s Method

The implied volatility \( \sigma_{	ext{impl}} \) is the value of \( \sigma \) that satisfies:

\[
C_{	ext{obs}} = C_{	ext{BS}}(S_0, X, T, r, \sigma)
\]

We solve this using the **Brent root-finding method** to find \( \sigma \) such that the difference between observed and theoretical price is zero.

---

### Vega (Sensitivity)

\[
	ext{Vega} = S_0 \cdot \sqrt{T} \cdot rac{1}{\sqrt{2\pi}} e^{-rac{d_1^2}{2}}
\]

This represents the sensitivity of the option price to changes in volatility.

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
