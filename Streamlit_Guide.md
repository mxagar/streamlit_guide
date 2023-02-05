# Streamlit Guide

This is a [Streamlit](https://streamlit.io/) guide in which 12 data science web apps as built. The original repository is from [Chanin Nantasenamat, Ph.D.](https://github.com/dataprofessor): [streamlit_freecodecamp](https://github.com/dataprofessor/streamlit_freecodecamp). The repository has also a [FreeCodeCamp](https://www.freecodecamp.org/) course by Dr. Nantasenamat: [Build 12 Data Science Apps with Python and Streamlit - Full Course](https://youtu.be/JwSS70SZdyM).

The present document is a basic guide for Streamlit based on that course. In addition, the file [`streamlit_summary_app.py`](streamlit_summary_app.py) is a summary app file, which doesn't run, bit which is a compilation of the most important commands.

Altogether, 12 apps are built (see co-located folders):

1. Simple Stock Price
2. Simple Bioinformatics DNA Count
3. EDA Basketball
4. EDA Football
5. EDA SP500 Stock Price
6. EDA Cryptocurrency
7. Classification Iris
8. Classification Penguin
9. Regression Boston Housing
10. Regression Bioinformatics Solubility
11. Deploy to Heroku

Table of contents:

- [Streamlit Guide](#streamlit-guide)
  - [0. Introduction and Setup](#0-introduction-and-setup)
    - [0.1 Basic File Structure and How to Run It](#01-basic-file-structure-and-how-to-run-it)
  - [1. App 1: Simple Stock Price Chart](#1-app-1-simple-stock-price-chart)
  - [2. App 2: DNA Count and Plot App](#2-app-2-dna-count-and-plot-app)
  - [3. App 3: NBA Team Statistics](#3-app-3-nba-team-statistics)
  - [4. App 4: NFL Team Statistics](#4-app-4-nfl-team-statistics)
  - [5. App 5: SP500 Stock EDA](#5-app-5-sp500-stock-eda)
  - [6. App 6: Cryptocurrency EDA](#6-app-6-cryptocurrency-eda)
  - [7. App 7: Iris Classification App](#7-app-7-iris-classification-app)
  - [Folders](#folders)

## 0. Introduction and Setup

With [Streamlit](https://streamlit.io/) we can:

- Build easily web apps with datasets.
- We can deploy those apps on the Streamlit platform or anywhere else. In particular, if we connect our Github account to Streamlit, the deployment is very easy.

Check the [gallery](https://streamlit.io/gallery), we'll see many functionalities being used:

- OpenCV apps
- Face-GAN apps (Tensorflow)
- Widgets (e.g., sliding bar)
- etc.

To install `streamlit`:

```bash
# Install
pip install streamlit

# Check: a web is opened in the browser with examples:
# http://localhost:8501
streamlit hello
```

### 0.1 Basic File Structure and How to Run It

Let's define our app in `myapp.py`:

```python
import streamlit as st
import pandas as pd

# Header text
# We add text in Markdown
st.write("""
# My App

This app is wonderful!

""")

# Load/get a dataset
df = pd.read_csv('data/dataset.csv')

# Add a header
st.write("""
## Variable `var1` line chart
""")
# Plot a line chart
st.line_chart(df['var1'])
```

To run that app, we execute:

```bash
cd /path/to/app
streamlit run myapp.py
# A web server is spun up and we see our app in the browser
# [http://localhost:](http://localhost:8501)
```

General notes:

- If we change something in the code (e.g., Markdown titles), the app will detect that and generate a `Re-run` button.
- Widgets will appear in order of definition in the main body or the side bar.
- If a widget introduces a variables user in later elements, those elements are refreshed or hidden to be created again with their associated widget (e.g., button)

## 1. App 1: Simple Stock Price Chart

The app file: [`app_1_simple_stock_price/myapp2.py`](app_1_simple_stock_price/myapp2.py).

Everything is shown in the basic file shown above: [0.1 Basic File Structure and How to Run It](#01-basic-file-structure-and-how-to-run-it). 

## 2. App 2: DNA Count and Plot App

The app file: [`app_2_simple_bioinformatics_dna/dna-app.py`](app_2_simple_bioinformatics_dna/dna-app.py).

In this app, the display of different types of variables (lists, dicts, dataframes) is shown, as well as how plotting works.

Everything is summarized in the main example app: [`streamlit_summary_app.py`](streamlit_summary_app.py).

## 3. App 3: NBA Team Statistics

The app file: [`app_3_eda_basketball/basketball_app.py`](app_3_eda_basketball/basketball_app.py).

Ver important app in which the following concepts are shown:

- How to fetch data from the web and actualize an internal dataset (cache)
- How to filter a dataset with variables entered in a sidebar (which is collapsable):
  - Drop down
  - Category selection
- How to filter internal datasets on entered variables and display them
- How to provide download links to internally generated datasets
- How to create buttons that trigger actions, e.g., plot on pressed

## 4. App 4: NFL Team Statistics

The app file: [`app_4_eda_football/basketball_app.py`](app_4_eda_football/football_app.py).

This app is very similar to the previous one; no new concepts are introduced.

## 5. App 5: SP500 Stock EDA

The app file: [`app_5_eda_sp500_stock/sp500-app.py`](app_5_eda_sp500_stock/sp500-app.py).

This app is very similar to the previous two; new concepts:

- Sidebar slider widget
- Downloading using the `yfinance` library
- Plotting several diagrams

## 6. App 6: Cryptocurrency EDA

The app file: [`app_6_eda_cryptocurrency/crypto-price-app.py`](app_6_eda_cryptocurrency/crypto-price-app.py).

This app is interesting, since it shows the following concepts:

- How to control page layout
- Expandable boxes
- How to perform web-scrapping on a real website using BeautifulSoup; more info: [Web Scraping Crypto Prices With Python](https://tommycc.medium.com/web-scraping-crypto-prices-with-python-41072ea5b5bf)

It's a cool application because it builds the dataset on-the-fly, i.e., it shows real updated data of cryptocurrency values fetched from Coinmarketcap using BeautifulSoup.

## 7. App 7: Iris Classification App

The app file: [`app_7_classification_iris/iris-ml-app.py`](app_7_classification_iris/iris-ml-app.py).

This is the first app in which a machine learning model is built and used. Apart from that, no really new concepts are shown. It's an interesting app because the model predicts based on user-controlled sliders, but probably, it's not the best example of deployment, because the model is trained when the app is opened; instead, we should load a pickle pipeline, for instance.

## Folders

```
app_8_classification_penguins
app_9_regression_boston_housing
app_10_regression_bioinformatics_solubility
```