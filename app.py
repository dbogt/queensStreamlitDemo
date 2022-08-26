import streamlit as st
import pandas as pd

st.title("Demo Dashbord")
st.write("Example dashboard in Marquee class for Queen's University")

#st.write is similar to print() in python

categories = ['A', 'B', 'C']
st.multiselect('pick an option', categories)

st.sidebar.button("Click me!")

url = "https://www.iposcoop.com/last-100-ipos/"
df = pd.read_html(url)[0]

#st.write(df)
st.dataframe(df)

#Dropdown menu that has all the unique Industries
#Filter the table for those selections
sectors = df['Industry'].unique() #remove duplicates
pickedSectors = st.multiselect('Pick a sector', sectors)

df_filtered = df[  df['Industry'].isin(pickedSectors)]
st.write(df_filtered)