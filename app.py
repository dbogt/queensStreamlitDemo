import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.title("Demo Dashbord")
st.write("Example dashboard in Marquee class for Queen's University")

#st.write is similar to print() in python

categories = ['A', 'B', 'C']
st.multiselect('pick an option', categories)

st.sidebar.button("Click me!")

@st.cache
def grabData():
    url = "https://www.iposcoop.com/last-100-ipos/"
    cachedTable = pd.read_html(url)[0]
    return cachedTable

df = grabData()

#st.write(df)
st.dataframe(df)

#Dropdown menu that has all the unique Industries
#Filter the table for those selections
sectors = df['Industry'].unique() #remove duplicates
pickedSectors = st.multiselect('Pick a sector', sectors)

df_filtered = df[  df['Industry'].isin(pickedSectors)]
st.write(df_filtered)


st.write("Plotly Demo")
import plotly.express as px
import plotly.graph_objects as go
df = px.data.medals_long()
nations = list(df['nation'].unique())
pickNations  = st.multiselect('Pick nation(s)', nations, nations)
filterDF = df[df['nation'].isin(pickNations)]

dfs = filterDF.groupby('medal').sum()
fig = px.bar(filterDF, x="medal", y="count", color="nation", text_auto=True)

fig.add_trace(go.Scatter(
    x=dfs.index, 
    y=dfs['count'],
    text=dfs['count'],
    mode='text',
    textposition='top center',
    textfont=dict(
        size=18,
    ),
    showlegend=False
))

fig.update_yaxes(range=[0,50])
st.plotly_chart(fig)