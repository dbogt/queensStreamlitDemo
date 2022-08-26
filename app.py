import streamlit as st
import pandas as pd

st.title("Demo Dashbord")
st.write("Example dashboard in Marquee class for Queen's University")

categories = ['A', 'B', 'C']
st.multiselect('pick an option', categories)

st.sidebar.button("Click me!")