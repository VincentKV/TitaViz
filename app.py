import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import pydeck as pdk
import seaborn as sns
import matplotlib


DATA_URL=("titanic.csv")

st.title("TitaViz")
st.markdown("")
st.markdown("This application is a Streamlit dashboard that can be used to visualize and analyse the famous titanic data.")

#@st.cache(persist=True)

data = pd.read_csv(DATA_URL)


if st.checkbox("Show Raw Data", True):
    st.subheader("Raw Data")
    st.write(data)


st.header("How are the passengers distributed?")

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

st.header("Who is most likely to survive?")


#st.write(data.describe())
#st.write(data.describe(include=['O']))
bla = st.selectbox('Type of passengers', ["Embarked","Sex","Pclass"])
st.write(data[[bla, 'Survived']].groupby([bla], as_index=False).mean().sort_values(by='Survived', ascending=False))



st.header("Is age a significative factor?")

#fig = px.bar(dfg)
#st.write(fig)

select = st.selectbox('Type of passengers', ["Survived","Sex","Pclass"])
fig = px.box(data, x=select, y="Age", points="all")
st.write(fig)