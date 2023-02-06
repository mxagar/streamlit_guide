"""Streamlit Summary App.

This is an example streamlit app
which doesn't run, but which collects
the most important streamlit functionalities
ready to copy & paste.

To install streamlit:

    $ pip install streamlit
    
To run an an app:

    $ streamlit run myapp.py 
    
... and the browser opened in http://localhost:8501

Detailed documentation:

    https://docs.streamlit.io/library/get-started

List of concepts:

- Display images
- Display Markdown text
- Expander bars (e.g., About)
- Headers, sub-headers
- Sidebar area (collapsable)
- Input text areas
- Showing python variables, dataframes, etc.
- Line charts
- Plots: altair, matplotlib, seaborn
- Fetching datasets, conditional on variables
- Refreshing fetched datasets: cache
- Downloading generated files/dataframes/CSVs
- Catching variables with widgets:
    - Dropdown: selectbox
    - Multiple categories: multiselect
    - Slider
- Button that creates actions
- Page layout:
    - Columns
    - Tabs
    - Grouping user input in functions
- File uploading
- Use of conditionals to control displayed app parts
- Example of loading and using a model pickle

Important examples:

- app_3_eda_basketball
- app_6_eda_cryptocurrency
- app_8_classification_penguins

For a deployment guide, check:

- Section 11 from Streamlit_Guide.md: Deployment to Heroku
- Section 12 from Streamlit_Guide.md: Deployment to Streamlit Share

General notes:

- If we change something in the code (e.g., Markdown titles), the app will detect that and generate a `Re-run` button.
- Widgets will appear in order of definition in the main body or the side bar.
- If a widget introduces a variables user in later elements, those elements are refreshed or hidden to be created again with their associated widget (e.g., button)
- Conditionals can be used to change the app parts which are displayed on-the-fly

Author: Mikel Sagardia
Date: 2023-02-04
"""

import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import base64
import pickle

# Load page/app logo
image = Image.open('logo.jpg')
# Display image; expand column width
st.image(image, use_column_width=True)

# Header text
# We can add text in Markdown
st.write("""
# My App

This **app** is **wonderful**!

""")

# About / Expander bar
expander_bar = st.expander("About")
expander_bar.markdown("""
Name, LinkedIn, Web, etc.
""")

# We can define any variables/structures
# and use any libraries; e.g.: 
# Load/get a dataset
df = pd.read_csv('data/dataset.csv')

# Add a header
st.write("""
## Variable `var1` line chart
""")
# Plot a line chart
st.line_chart(df['var1'])

# Headers
# Note that we can put everythin on the main body
# or on the siderbar!
#st.sidebar.header('My header')
st.header('My header')
st.subheader('My subheader')

# Markdown Text
# Another way of writing text
st.markdown("""
## Header

My text.
""")

# Input text
default_input = "bla bla"
#input_text = st.sidebar.text_area("Sequence input", default_input, height=250)
input_text = st.text_area("Input text", default_input, height=250)

# We can print variables just by invoking them
# but they are not formatted as text.
# Use st.write() for text-style.
my_list = [1, 2, 3]
my_list # list is displayed!
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict # dict is displayed!

# (Pandas) data frames are nicely formatted and displayed as tables
st.write(df)

# Horizontal line in Markdown
st.write("""
***
""")

# Plot Matplotlib/Seaborn figure
# Always catch fig and pass it to st.pyplot()
fig = plt.figure()
plt.plot([1,2,3], [1,2,3])
sns.lineplot(x=[1,2,3],y=[3,2,1])
st.pyplot(fig)

# Plot with altair: bar chart
# More on altair: https://altair-viz.github.io/index.html
df = pd.DataFrame({'name': ['a', 'b', 'c'], 'count': [1, 2, 3]})
p = alt.Chart(df).mark_bar().encode(
    x='name',
    y='count'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)

## Dataframe filtering: select key variable, year
# Example: app_3_eda_basketball
# Sidebar drop down widget - Feature value selection: Year
st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950,2020))))

## Web-scrapping: Fetch data frm HTML/web conditional on variable and refresh!
# Caching: https://docs.streamlit.io/library/api-reference/performance/st.cache
# Example: app_3_eda_basketball
@st.cache # Run every time we change function name / code / parameter values (year) and store results in local cache
def load_data(year):
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
    html = pd.read_html(url, header = 0)
    df = html[0]
    # Do all the pre-processing you need here...
    df = df.fillna(0)
    return df
df = load_data(selected_year)

## Dataframe filtering
# Use side panel to select categorical feature values
# Then, filter dataframe and show it
# Example: app_3_eda_basketball, app_5_eda_sp500_stock
# Sidebar multiselection widget - Team selection
teams = sorted(df.team.unique())
selected_teams = st.sidebar.multiselect('Teams', teams, teams) # name, all options/categories, default options/categories
# Sidebar slider widget - Team selection
num_members = st.sidebar.slider('Minimum members', 20, 50, 30) # min, max, default
# Sidebar multiselection widget - Position selection
positions = ['C','PF','SF','PG','SG']
selected_positions = st.sidebar.multiselect('Position', positions, positions)
# Filter and display dataframe
df_filtered = df[(df.team.isin(selected_teams) & df.position.isin(selected_positions) & df.members >= num_members)]
st.dataframe(df_filtered)

## Button to display heatmap
# Example: app_3_eda_basketball
if st.button('Correlation Heatmap'):
    st.header('Correlation Heatmap')
    # It might not work if we don't save & load the df
    # Maybe it's because of some type issues?
    df.to_csv('output.csv',index=False)
    df = pd.read_csv('output.csv')
    corr = df.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        fig, ax = plt.subplots(figsize=(7, 5))
        ax = sns.heatmap(corr, mask=mask, vmax=1, square=True)
    st.pyplot(fig)
    
## File download, e.g., generated/filtered CSV
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
# df passed, encoded to bytes as b64
# then downloaded as dataset.csv
# We can modify the name of the downloaded file changing "dataset.csv"
# Download functionality is shown as a Markdown link
# Example: app_3_eda_basketball
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="dataset.csv">Download CSV File</a>'
    return href
st.markdown(filedownload(df_filtered), unsafe_allow_html=True)

## Page layout: Columns
# We can divide the page in columns
# The sidebar is the first column and it can be collapsed
# The rest of the columns is defined with relative size
# Example: app_6_eda_cryptocurrency
st.set_page_config(layout="wide") # Expand app to full width
col1 = st.sidebar # the sidebar is a collapsable col
col2, col3 = st.columns((2,1)) # 2:1 size ratio, i.e., col2 is 2x width compared to col3
# Then, instead of defining widgets/elements with st.element
# we do it with the columns:
col1.header("Header 1")
col2.subheader("Header 2")
selected_letter = col1.selectbox("Choose letter", ('A', 'B', 'C'))
selected_coin = col1.multiselect('Coin', ['USD', 'EUR'], ['USD', 'EUR'])
col3.write("""...""")
col2.markdown("""...""")
col2.dataframe(df)
col3.pyplot(fig)
# ...

## Page layout: Tabs
tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])
with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

## Page layout: packing user input features into a function
# Example: app_7_classification_iris
def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4) # min, max, default
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features
    # Then we pass features to a model for prediction!

## Upload a file with dataset / Use user input from sidebar
# The following snippet tries to upload a CSV from the user (and provides an example CSV as a link)
# If the CSV is not uploaded by the user, the input from the sliders is taken
# Example: app_8_classification_penguins
st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/penguins_example.csv)
""")
# Collects user input features into dataframe
# Conditionals can be used to change displayed app parts on-the-fly
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    # No file uploaded, take user input from sliders
    def user_input_features():
        # Penguins dataset
        island = st.sidebar.selectbox('Island',('Biscoe','Dream','Torgersen'))
        sex = st.sidebar.selectbox('Sex',('male','female'))
        bill_length_mm = st.sidebar.slider('Bill length (mm)', 32.1,59.6,43.9)
        bill_depth_mm = st.sidebar.slider('Bill depth (mm)', 13.1,21.5,17.2)
        flipper_length_mm = st.sidebar.slider('Flipper length (mm)', 172.0,231.0,201.0)
        body_mass_g = st.sidebar.slider('Body mass (g)', 2700.0,6300.0,4207.0)
        data = {'island': island,
                'bill_length_mm': bill_length_mm,
                'bill_depth_mm': bill_depth_mm,
                'flipper_length_mm': flipper_length_mm,
                'body_mass_g': body_mass_g,
                'sex': sex}
        features = pd.DataFrame(data, index=[0])
        return features
    input_df = user_input_features()

## Load model pickle + perform inference
# Example: app_8_classification_penguins
# Reads in saved classification model
load_clf = pickle.load(open('penguins_clf.pkl', 'rb'))
# Apply model to make predictions
prediction = load_clf.predict(df)
prediction_proba = load_clf.predict_proba(df)
st.subheader('Prediction')
penguins_species = np.array(['Adelie','Chinstrap','Gentoo'])
st.write(penguins_species[prediction])
st.subheader('Prediction Probability')
st.write(prediction_proba)
