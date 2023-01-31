
import streamlit as st
import pandas as pd

st.set_page_config(page_title='Herramientas digitales en español')
st.title('Empoweringrace')

st.title('Herramientas digitales en español')
df=pd.read_csv('datos.csv')
df=df.drop(columns='Unnamed: 0',axis=1)

imagen1=df['Imagenes_url'][0]+'.jpg'

col1, col2, col3 = st.columns(3)

with col1:
   st.header(df.iloc[0][0])
   st.image(df.iloc[0][3])
   st.title(df.iloc[0][2]])
   

with col2:
   st.header(df.iloc[1][0])
   st.image(df.iloc[1][3])

with col3:
   st.header(df.iloc[2][0])
   st.image(df.iloc[2][3])
