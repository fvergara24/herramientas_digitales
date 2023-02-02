
import streamlit as st
import pandas as pd

st.set_page_config(page_title='Herramientas digitales en español')
st.title('Empoweringrace')

st.title('Herramientas digitales en español')
df=pd.read_csv('datos.csv')
df=df.drop(columns='Unnamed: 0',axis=1)

#imagen1=df['Imagenes_url'][0]+'.jpg'

col1, col2= st.columns(2)

with col1:
   st.header(df.iloc[0][0])
   st.caption(df.iloc[0][1])
   #st.image(df.iloc[0][3], caption=df.iloc[0][3], use_column_width='auto')
   
with col2:
   st.header(df.iloc[1][0])
   st.caption(df.iloc[1][1])
   #st.image(df.iloc[1][3], caption=df.iloc[1][2])

st.dataframe(data=df)

st.table(df)
