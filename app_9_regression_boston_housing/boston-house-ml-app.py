import streamlit as st
import pandas as pd
import shap
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.ensemble import RandomForestRegressor
import numpy as np

st.write("""
# Boston House Price Prediction App

This app predicts the **Boston House Price**!
""")
st.write('---')

# Loads the Boston House Price Dataset
#boston = datasets.load_boston()
#X = pd.DataFrame(boston.data, columns=boston.feature_names)
#Y = pd.DataFrame(boston.target, columns=["MEDV"])
# Due to an ethics issue, the Boston dataset needs to be downloaded manually
# from http://lib.stat.cmu.edu/datasets/boston
feature_dict = {
    'CRIM': "per capita crime rate by town",
    'ZN': "proportion of residential land zoned for lots over 25,000 sq.ft.",
    'INDUS': "proportion of non-retail business acres per town",
    'CHAS': "Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)",
    'NOX': "nitric oxides concentration (parts per 10 million)",
    'RM': "average number of rooms per dwelling",
    'AGE': "proportion of owner-occupied units built prior to 1940",
    'DIS': "weighted distances to five Boston employment centres",
    'RAD': "index of accessibility to radial highways",
    'TAX': "full-value property-tax rate per $10,000",
    'PTRATIO': "pupil-teacher ratio by town",
    'B': "1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town",
    'LSTAT': "percentage lower status of the population",
    'MEDV': "Median value of owner-occupied homes in $1000's"
}
feature_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]
X = pd.DataFrame(data, columns=feature_names)
Y = pd.DataFrame(target, columns=["MEDV"])
X = X.astype('float64')
Y = Y.astype('float64')

# Sidebar
# Header of Specify Input Parameters
st.sidebar.header('Specify Input Parameters')

def user_input_features():
    CRIM = st.sidebar.slider('CRIM', float(X.CRIM.min()), float(X.CRIM.max()), float(X.CRIM.mean()))
    ZN = st.sidebar.slider('ZN', float(X.ZN.min()), float(X.ZN.max()), float(X.ZN.mean()))
    INDUS = st.sidebar.slider('INDUS', float(X.INDUS.min()), float(X.INDUS.max()), float(X.INDUS.mean()))
    CHAS = st.sidebar.slider('CHAS', float(X.CHAS.min()), float(X.CHAS.max()), float(X.CHAS.mean()))
    NOX = st.sidebar.slider('NOX', float(X.NOX.min()), float(X.NOX.max()), float(X.NOX.mean()))
    RM = st.sidebar.slider('RM', float(X.RM.min()), float(X.RM.max()), float(X.RM.mean()))
    AGE = st.sidebar.slider('AGE', float(X.AGE.min()), float(X.AGE.max()), float(X.AGE.mean()))
    DIS = st.sidebar.slider('DIS', float(X.DIS.min()), float(X.DIS.max()), float(X.DIS.mean()))
    RAD = st.sidebar.slider('RAD', float(X.RAD.min()), float(X.RAD.max()), float(X.RAD.mean()))
    TAX = st.sidebar.slider('TAX', float(X.TAX.min()), float(X.TAX.max()), float(X.TAX.mean()))
    PTRATIO = st.sidebar.slider('PTRATIO', float(X.PTRATIO.min()), float(X.PTRATIO.max()), float(X.PTRATIO.mean()))
    B = st.sidebar.slider('B', float(X.B.min()), float(X.B.max()), float(X.B.mean()))
    LSTAT = st.sidebar.slider('LSTAT', float(X.LSTAT.min()), float(X.LSTAT.max()), float(X.LSTAT.mean()))
    data = {'CRIM': CRIM,
            'ZN': ZN,
            'INDUS': INDUS,
            'CHAS': CHAS,
            'NOX': NOX,
            'RM': RM,
            'AGE': AGE,
            'DIS': DIS,
            'RAD': RAD,
            'TAX': TAX,
            'PTRATIO': PTRATIO,
            'B': B,
            'LSTAT': LSTAT}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

# Main Panel

# Print specified input parameters
st.header('Specified Input parameters')
st.write(df)
st.write('---')

# Build Regression Model
model = RandomForestRegressor()
model.fit(X, Y)
# Apply Model to Make Prediction
prediction = model.predict(df)

st.header('Prediction of MEDV')
st.write(prediction)
st.write('---')

# Explaining the model's predictions using SHAP values
# https://github.com/slundberg/shap
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

st.header('Feature Importance')
fig1 = plt.figure()
plt.title('Feature importance based on SHAP values')
shap.summary_plot(shap_values, X)
st.pyplot(fig1, bbox_inches='tight')
st.write('---')

fig2 = plt.figure()
plt.title('Feature importance based on SHAP values (Bar)')
shap.summary_plot(shap_values, X, plot_type="bar")
st.pyplot(fig2, bbox_inches='tight')
