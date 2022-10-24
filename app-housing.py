import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')
st.title('California Housing Data(1990) by Ziyi Zhao')
df = pd.read_csv('housing.csv')

value_slider = st.slider('Median Housing Price', 0.0, 500001.0, 200000.0)
st.header('See more filters in the sidebar:')

location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  
     df.ocean_proximity.unique())  

df = df[df.median_house_value <= value_slider]
df = df[df.ocean_proximity.isin(location_filter)]

genre = st.sidebar.radio(
    "Choose income level",
    ('Low', 'Medium', 'High'))

if genre == 'Low':
    df = df[df.median_income <= 2.5]
elif genre == 'Medium':
    df = df[df.median_income > 2.5]
    df = df[df.median_income < 4.5]
elif genre == 'High':
    df = df[df.median_income >= 4.5]

st.map(df)
fig, ax = plt.subplots()
df.median_house_value.hist(bins=30)
st.header('Histgram of median house value')
st.pyplot(fig)






