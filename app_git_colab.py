
import streamlit as st
import pandas as pd

st.set_page_config(page_title='Herramientas digitales en español')
st.title('Empoweringrace')

st.title('Herramientas digitales en español')
df=pd.read_csv('/content/herramientas_digitales/datos.csv')
df=df.drop(columns='Unnamed: 0',axis=1)
st.dataframe(data=df)
st.title('dataframe')
