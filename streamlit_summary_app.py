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

Author: Mikel Sagardia
Date: 2023-02-04
"""

import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

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


