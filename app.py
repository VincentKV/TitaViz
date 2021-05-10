import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import pydeck as pdk
import seaborn as sns
import matplotlib


DATA_URL=("titanic.csv")

st.title("OrthoViz : Interactive visualization of patients data")
st.markdown("")
st.markdown("This application is a Streamlit dashboard that can me used to analyse motor vehicle collisions in NYC")

#@st.cache(persist=True)

data = pd.read_csv(DATA_URL)




st.header("Where are the most people injured in NYC?")


if st.checkbox("Show Raw Data", False):
    st.subheader("Raw Data")
    st.write(data)

#st.write(data.describe())
#st.write(data.describe(include=['O']))
bla = st.selectbox('Affected type of people', ["Embarked","Sex","Pclass"])
st.write(data[[bla, 'Survived']].groupby([bla], as_index=False).mean().sort_values(by='Survived', ascending=False))


dfg=data.groupby('Sex').count().reset_index()
dfg=dfg.rename(columns={"PassengerId": "Passengers"})
fig = px.bar(dfg,
             x='Sex',
             y='Passengers',
             title='Test',
             #color='Items',
             barmode='stack')
st.write(fig)


Nbins = st.slider("Bins",2,42)

#fig = px.histogram(data, x="Age", nbins=Nbins-1)
#st.write(fig)
fig = px.histogram(data, x="Age", color="Sex", marginal="rug",nbins=Nbins-1,hover_data=data.columns)
st.write(fig)


#fig = px.bar(dfg)
#st.write(fig)

select = st.selectbox('Affected type of people', ["Survived","Sex","Pclass"])
fig = px.box(data, x=select, y="Age", points="all")
st.write(fig)