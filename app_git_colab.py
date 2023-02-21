
import streamlit as st
import pandas as pd

st.set_page_config(page_title='Herramientas digitales en español', page_icon='favicon.jpg')
st.image('Logo.jpg')
st.title('Herramientas digitales en español')


df=pd.read_csv('datos.csv')
df=df.drop(columns='Unnamed: 0',axis=1)

df_columna1=df.iloc[:round(len(df)/2),:]
df_columna2=df.iloc[round(len(df)/2):,:]

#imagen1=df['Imagenes_url'][0]+'.jpg'

text=st.text_input('Buscar aplicaciones','')
#st.markdown(f'buscaste {text}')
if text:
  mask = df['Descripcion'].str.contains(text)
  df_busqueda = df[mask]
  df_busqueda = df_busqueda.reset_index(drop=True)
  for j in range(len(df_busqueda)):
    st.write(f"{[df_busqueda.iloc[j][0]]}(%s)" % df_busqueda.iloc[j][2])
    st.caption(df_busqueda.iloc[j][1])
    #st.image(df_busqueda.iloc[j][3], caption=df_busqueda.iloc[j][3], use_column_width='auto')

else:
  col1, col2= st.columns(2)

  with col1:
     for i in range(len(df_columna1)):
      st.write(f"{[df_columna1.iloc[i][0]]}(%s)" % df_columna1.iloc[i][2])
      st.caption(df_columna1.iloc[i][1])
      #st.image(df_columna1.iloc[0][3], caption=df_columna1.iloc[0][3], use_column_width='auto')
      
  with col2:
     for i in range(len(df_columna2)):
      st.write(f"{[df_columna2.iloc[i][0]]}(%s)" % df_columna2.iloc[i][2])
      st.caption(df_columna2.iloc[i][1])
      #st.image(df_columna2.iloc[1][3], caption=df_columna2.iloc[1][2])





