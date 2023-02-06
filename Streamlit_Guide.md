# Streamlit Guide

This is a [Streamlit](https://streamlit.io/) guide in which 12 data science web apps as built. The original repository is from [Chanin Nantasenamat, Ph.D.](https://github.com/dataprofessor): [streamlit_freecodecamp](https://github.com/dataprofessor/streamlit_freecodecamp). The repository has also a [FreeCodeCamp](https://www.freecodecamp.org/) course by Dr. Nantasenamat: [Build 12 Data Science Apps with Python and Streamlit - Full Course](https://youtu.be/JwSS70SZdyM).

The present document is a basic guide for Streamlit based on that course. In addition, the file [`streamlit_summary_app.py`](streamlit_summary_app.py) is a summary app file, which doesn't run, bit which is a compilation of the most important commands.

Altogether, these apps are built (see co-located folders; most important apps in bold):

1. Simple Stock Price
2. Simple Bioinformatics DNA Count
3. **EDA Basketball**
4. EDA Football
5. EDA SP500 Stock Price
6. **EDA Cryptocurrency**
7. Classification Iris
8. **Classification Penguin**
9. Regression Boston Housing
10. Regression Bioinformatics Solubility
11. **Deploy to Heroku**
12. Deploy to Streamlit Share

Additionally, check the following app I deployed using `streamlit`:

[https://github.com/mxagar/course_recommender_streamlit](https://github.com/mxagar/course_recommender_streamlit)

Table of contents:

- [Streamlit Guide](#streamlit-guide)
  - [0. Introduction and Setup](#0-introduction-and-setup)
    - [0.1 Basic File Structure and How to Run It](#01-basic-file-structure-and-how-to-run-it)
    - [0.2 How Should I Use this Guide?](#02-how-should-i-use-this-guide)
  - [1. App 1: Simple Stock Price Chart](#1-app-1-simple-stock-price-chart)
  - [2. App 2: DNA Count and Plot App](#2-app-2-dna-count-and-plot-app)
  - [3. App 3: NBA Team Statistics](#3-app-3-nba-team-statistics)
  - [4. App 4: NFL Team Statistics](#4-app-4-nfl-team-statistics)
  - [5. App 5: SP500 Stock EDA](#5-app-5-sp500-stock-eda)
  - [6. App 6: Cryptocurrency EDA](#6-app-6-cryptocurrency-eda)
  - [7. App 7: Iris Classification App](#7-app-7-iris-classification-app)
  - [8. App 8: Penguin Classification App](#8-app-8-penguin-classification-app)
  - [9. App 9: Boston Housing App](#9-app-9-boston-housing-app)
  - [10. App 10: Molecular Solubility Prediction App](#10-app-10-molecular-solubility-prediction-app)
  - [11. Deployment to Heroku](#11-deployment-to-heroku)
    - [Files](#files)
      - [`.slugignore`](#slugignore)
      - [`Procfile`](#procfile)
      - [`setup.sh`](#setupsh)
      - [`runtime.txt`](#runtimetxt)
      - [`requirements.txt`](#requirementstxt)
    - [Deployment Process](#deployment-process)
  - [12. Deployment to Streamlit Share](#12-deployment-to-streamlit-share)

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
- If a widget introduces a variables user in later elements, those elements are refreshed or hidden to be created again with their associated widget (e.g., button).
- Conditionals can be used to change the app parts which are displayed on-the-fly.

### 0.2 How Should I Use this Guide?

First, have look at the summary script: [`streamlit_summary_app.py`](streamlit_summary_app.py).

Then, check these apps:

- [3. App 3: NBA Team Statistics](#3-app-3-nba-team-statistics)
- [6. App 6: Cryptocurrency EDA](#6-app-6-cryptocurrency-eda)
- [8. App 8: Penguin Classification App](#8-app-8-penguin-classification-app)

Finally, use the summary script to build your app: [`streamlit_summary_app.py`](streamlit_summary_app.py).

And, if you want to deploy your app, check:

- [11. Deployment to Heroku](#11-deployment-to-heroku)
- [12. Deployment to Streamlit Share](#12-deployment-to-streamlit-share)

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

I had to fix the web-scrapping code, because the Coinmarketcap web has changed.

## 7. App 7: Iris Classification App

The app file: [`app_7_classification_iris/iris-ml-app.py`](app_7_classification_iris/iris-ml-app.py).

This is the first app in which a machine learning model is built and used. Apart from that, no really new concepts are shown. It's an interesting app because the model predicts based on user-controlled sliders, but probably, it's not the best example of deployment, because the model is trained when the app is opened; instead, we should load a pickle pipeline, for instance.

## 8. App 8: Penguin Classification App

The app file: [`app_8_classification_penguins/penguins-app.py`](app_8_classification_penguins/penguins-app.py).

This is a machine learning application app in which Penguins are classified based on 4 numerical and 2 categorical variables. The original dataset can be downloaded from [allisonhorst/palmerpenguins](https://github.com/allisonhorst/palmerpenguins). The app is very improvable in terms of production readiness, but it's a nice example of the basic tools available on Streamlit to build an app. Data processing and modeling are done separately.

The repository has a companion files:

- [`penguins_example.csv`](app_8_classification_penguins/penguins_example.csv): example CSV, in case the user uploads a CSV, so that he/she keeps to the format
- [`penguins_cleaned.csv`](app_8_classification_penguins/penguins_cleaned.csv): training dataset
- [`penguins-model-building.py`](app_8_classification_penguins/penguins-model-building.py): model pickle is built
- [`penguins_clf.pkl`](app_8_classification_penguins/penguins_clf.pkl): model pickle

New concepts:

- A model pickle is loaded; we should similarly load the processing pipeline
- File upload widget

## 9. App 9: Boston Housing App

The app file: [`app_9_regression_boston_housing/boston-house-ml-app.py`](app_9_regression_boston_housing/boston-house-ml-app.py).

The Boston housing dataset is used to train a random forest and its feature importances are analyzed. Nothing really new is done here. The example is not optimal, because the dataset is downloaded, then the model trained and finally the inference and analysis done &mdash; all in one file.

I had to fix the dataset acquisition, because Boston is not included in Scikit-Learn anymore due to an ethical issue.

## 10. App 10: Molecular Solubility Prediction App

The app file: [`app_10_regression_bioinformatics_solubility/solubility-app.py`](app_10_regression_bioinformatics_solubility/solubility-app.py).

The repository has a companion files: a notebook (where the model pickle is created), a logo JPEG, and a model PKL.

A sequence of molecules is input and its solubility is predicted with a previously created regression model.

Nothing new is used here; perhaps the characteristic property of this example is the fact that custom functions are written which are used to transform the data for the model.

## 11. Deployment to Heroku

In this example a Github deployment is done to Heroku: we create an app in Heroku, link a Github repository with the `streamlit` app file to it and deploy it *continuously* whenever we push the code to the repo.

As mentioned, the Github repository needs to contain a web app based on `streamlit`; to keep things easy, I'll take this very repository but I'll deploy only the penguins app, so the web app will be: [`app_8_classification_penguins/penguins-app.py`](app_8_classification_penguins/penguins-app.py). A Github repository which contains only the app is [penguins-heroku](https://github.com/dataprofessor/penguins-heroku).

For any Heroku deployment we need to prepare the following deployment files, which are present in the current repository:

- [`.slugignore`](.slugignore): which files from the repo should be ignored for the Heroku deployment.
- [`Procfile`](Procfile): Heroku app command.
- [`setup.sh`](setup.sh): setup for streamlit.
- [`runtime.txt`](runtime.txt): Python version for Heroku deployment.
- [`requirements.txt`](requirements.txt): requirements for the app.

In addition to those files and the web app, we also need any files that the web app might require. In order to make things easier, I link the files to the repository root from the folder `app_8_classification_penguins`. In a regular situation, the deployed repository should resolve the paths without links.

```
penguins-app.py -> app_8_classification_penguins/penguins-app.py
penguins_cleaned.csv -> app_8_classification_penguins/penguins_cleaned.csv
penguins_clf.pkl -> app_8_classification_penguins/penguins_clf.pkl
penguins_example.csv -> app_8_classification_penguins/penguins_example.csv
```

In the following, I explain first how to create those deployment files. Then, the deployment process is explained.

### Files

#### [`.slugignore`](.slugignore)

All files which need to be ignored in the deployment; recall that we have a 500 MB slug size limit in Heroku. In this case:

```
eda_fe_summary
app_1_simple_stock_price
app_2_simple_bioinformatics_dna
app_3_eda_basketball
app_4_eda_football
app_5_eda_sp500_stock
app_6_eda_cryptocurrency
app_7_classification_iris
app_9_regression_boston_housing
app_10_regression_bioinformatics_solubility
Streamlit_Guide.md
streamlit_summary_app.py
README.md
```

#### [`Procfile`](Procfile)

Command to run when the dyno is spun up. In this case, two commands are run:

1. First, a `streamlit` configuration file is created with `setup.sh`
2. Then, the `streamlit` app is run as always

Thus:

```
web: sh setup.sh && streamlit run penguins-app.py
```

Note that I made a link of the app file and the required archives to the root, so that that command `streamlit run penguins-app.py` can be run:

```
penguins-app.py -> app_8_classification_penguins/penguins-app.py
penguins_cleaned.csv -> app_8_classification_penguins/penguins_cleaned.csv
penguins_clf.pkl -> app_8_classification_penguins/penguins_clf.pkl
penguins_example.csv -> app_8_classification_penguins/penguins_example.csv
```

#### [`setup.sh`](setup.sh)

A setup bash script which creates the `streamlit` configuration file; we could add that file to our repository, too, I guess.

```bash
mkdir -p ~/.streamlit/
echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml
```

More on `streamlit` configuration: [Streamlit Configuration](https://docs.streamlit.io/library/advanced-features/configuration).

#### [`runtime.txt`](runtime.txt)

Python version to be run. Heroku has limitations in that respect: [Heroku: Supported Python Runtimes](https://devcenter.heroku.com/articles/python-support#supported-runtimes). The environment in which we develop locally should have that Python version, too.

```bash
python --version # 3.9.16, supported in all stacks (Heroku)
```

Thus:

```
python-3.9.16
```

#### [`requirements.txt`](requirements.txt)

Any libraries which are necessary to run the deployed app; usually, the imports are a good hint. To get the local dependency versions, we can run:

```bash
pip freeze # > requirements.txt
conda list # > conda_packages.txt
```

In our case, we have these dependencies:

```
streamlit==1.17.0
pandas==1.5.3
numpy==1.23.5
scikit-learn==1.2.1
```

### Deployment Process

Any Heroku deployment is very easy. To create an app (*slug* in Heroku), we can work with the CLI or using the GUI. In the following, I will explain how to do it via the web GUI. For more information, visit these guides:

- [`MLOpsND_Deployment.md`: Continuous Deployment with Heroku](https://github.com/mxagar/mlops_udacity/blob/main/03_Deployment/MLOpsND_Deployment.md#44-continuous-deployment-with-heroku)
- [`MLOpsND_Deployment.md`: Heroku CLI](https://github.com/mxagar/mlops_udacity/blob/main/03_Deployment/MLOpsND_Deployment.md#54-heroku-revisited-procfiles-and-cli)

Step by step guide to deploy the app `penguins-app-streamlit`:

- Log in to Heroku (we need to have an account and a subscription)
- New: Create new app (Europe / US)
- Select name, e.g., ``penguins-app-streamlit``
- Deployment method: we choose `Github`
  - Connect to Github, authorize / grant access
  - Select repository: `streamlit_guide`
  - Connect
- Automatic deploys
  - Choose branch: `main` (or another)
  - If we had CI (Github actions), we'd wait for it to pass before deploying
  - Enable automatic deploys: every time we push to the branch (and tests pass, if any) the code is deployed on Heroku
- Then, the app will be deployed automatically right away; however, note that:
  - If we have no `Procfile`, the slug will be deployed, but nothing will happen (a default blank app is launched).
  - If we have no executable code, nothing will happen (a default blank app is launched).
- Manual deploy: we can also deploy manually clicking on the button `Deploy Branch`!

We can **check the Heroku app in the web GUI**: We select the app in the main dashboard and:

- Open App: App management dashboard is shown
- More > View logs: logs of deployment are shown
  - If we have no `Procfile`, the slug will be deployed, but nothing will happen (a default blank app is launched); the logs will reflect that

After the deployment is done (10-15 mins later), we get the link to the app:

[https://penguins-app-streamlit.herokuapp.com/](https://penguins-app-streamlit.herokuapp.com/)


## 12. Deployment to Streamlit Share

The Streamlit deployment is even easier as the Heroku deployment, but not as powerful. Also note that I haven't found any way to use something similar to `.streamlitignore`, so be careful with the size of the repository.

In the Youtube video, the SP500 app is deployed:

[streamlit-10](https://github.com/dataprofessor/streamlit-10)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/streamlit-10/main/sp500-app.py)

However, I deployed the same penguins app as in the Heroku case.

To deploy it in Streamlit share, we need to go to [https://share.streamlit.io/](https://share.streamlit.io/). There, we create an account and link our Github account. The process is similar as with Heroku: we link a Github repo which should contain the main app. Additionally, we need to have a `requirements.txt` file with all the dependencies. Therefore, the links created in the previous section (Heroku deployment) should still work. We can check that everything is fine by running the app locally: `streamlit run penguins-app.py`. When everything is set up, we click on `New app` and we fill in the form:

- Repository: `mxagar/streamlit_guide`
- Branch: `main`
- Main file path: `penguins-app.py`
- Advanced settings:
  - Python version: `3.9`
  - (Secrets using TOML format)
- Deploy! We get the side panel `Manage`, where we see how the app is being deployed.

After the deployment is done, we get the link to the app. We can embed the link in a badge using the pattern above.

:warning: The deployment took in my case very long with the complete repository and the links and it didn't really complete. I think that [Streamlit Share](https://share.streamlit.io/) is conceived for much smaller and slim apps. That, or the links don't work.