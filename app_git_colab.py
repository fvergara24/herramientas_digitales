
import streamlit as st
import pandas as pd
import webbrowser
from bokeh.models.widgets import Div

st.set_page_config(page_title='Herramientas digitales en español')
st.title('Empoweringrace')

st.title('Herramientas digitales en español')
df=pd.read_csv('datos.csv')
df=df.drop(columns='Unnamed: 0',axis=1)

df_columna1=df.iloc[:round(len(df)/2),:]
df_columna2=df.iloc[round(len(df)/2):,:]

#imagen1=df['Imagenes_url'][0]+'.jpg'

if st.button('Página'):
    js = "window.open('https://www.streamlit.io/')"  # New tab or window
    js = "window.location.href = 'https://www.streamlit.io/'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)


col1, col2= st.columns(2)

with col1:
   for i in range(len(df_columna1)):
    
    #st.button(df_columna1.iloc[i][0], help=df_columna1.iloc[i][2])
    st.caption(df_columna1.iloc[i][1])
    #st.image(df_columna1.iloc[0][3], caption=df_columna1.iloc[0][3], use_column_width='auto')
    
with col2:
   for i in range(len(df_columna2)):
    st.button(df_columna2.iloc[i][0], help=df_columna1.iloc[i][2])
    st.caption(df_columna2.iloc[i][1])
    #st.image(df_columna2.iloc[1][3], caption=df_columna2.iloc[1][2])
