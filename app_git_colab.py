
import streamlit as st
import pandas as pd

st.set_page_config(page_title='Herramientas digitales en español')
st.title('Empoweringrace')

st.title('Herramientas digitales en español')
df=pd.read_csv('datos.csv')
df=df.drop(columns='Unnamed: 0',axis=1)
st.title('Tabla')
st.dataframe(data=df)


col1, col2, col3 = st.columns(3)

with col1:
   st.header(df['Nombres'][0])
   st.image("df['Imagenes_url][0]+'.jpg'")
   

with col2:
   st.header(df['Nombres'][1])
   

with col3:
   st.header(df['Nombres'][2])
   
