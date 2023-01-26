
import streamlit as st
import pandas as pd

st.set_page_config(page_title='Herramientas digitales en español')
st.title('Empoweringrace')

st.title('Herramientas digitales en español')
df=pd.read_csv('datos.csv')
df=df.drop(columns='Unnamed: 0',axis=1)
st.title('Tabla')
st.dataframe(data=df)

imagen1=df['Imagenes_url'][0]+'.jpg'

col1, col2, col3 = st.columns(3)

with col1:
   st.header(df['Nombres'][0])
   st.image(imagen1)
   

with col2:
   st.header(df['Nombres'][1])
   st.image(df['Imagenes_url'][1]+'.jpg')

with col3:
   st.header(df['Nombres'][2])
   st.image(df['Imagenes_url'][3]+'.jpg')
