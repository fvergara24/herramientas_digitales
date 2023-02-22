
import streamlit as st
import pandas as pd

st.set_page_config(page_title='Herramientas digitales en español', page_icon='favicon.jpg')
st.image('Logo.jpg')
st.title('Herramientas digitales en español')


df=pd.read_csv('datos_todos.csv')
df=df.drop(columns='Unnamed: 0',axis=1)

df_columna1=df.iloc[:round(len(df)/2),:]
df_columna2=df.iloc[round(len(df)/2):,:]


#imagen1=df['Imagenes_url'][0]+'.jpg'

text=st.text_input('Buscar aplicaciones','')
text = text.lower()

if text:
    mask = df['Descripcion'].str.contains(text)
    contador=0
    for i in range(len(mask)): 
      if mask.loc[i]==False:
        contador+=1
    if contador==len(mask):
      st.write('No hay coincidencias')
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
        #original_title = '<p style="font-family:Courier; color:Blue; font-size: 20px;">f"{[df_columna1.iloc[i][0]]}(%s)" % df_columna1.iloc[i][2]</p>'
        #st.markdown(original_title, unsafe_allow_html=True) 
        st.write(f"{[df_columna1.iloc[i][0]]}(%s)" % df_columna1.iloc[i][2])
        st.caption(df_columna1.iloc[i][1])
        #st.image(df_columna1.iloc[0][3], caption=df_columna1.iloc[0][3], use_column_width='auto')
        
    with col2:
      for i in range(len(df_columna2)):
        st.write(f"{[df_columna2.iloc[i][0]]}(%s)" % df_columna2.iloc[i][2])
        st.caption(df_columna2.iloc[i][1])
        #st.image(df_columna2.iloc[1][3], caption=df_columna2.iloc[1][2])


# CATEGORIAS
#df_3d=pd.read_csv('3D.csv')
#df_3d=df_3d.drop(columns='Unnamed: 0',axis=1)
#art=pd.read_csv('art.csv')
#art=art.drop(columns='Unnamed: 0',axis=1)
#Audio=pd.read_csv('audio.csv')
#Audio=Audio.drop(columns='Unnamed: 0',axis=1)
#code_assistant=pd.read_csv('code_assistant.csv')
#code_assistant=code_assistant.drop(columns='Unnamed: 0',axis=1)

def funcion_categoria(nombre):
  nombre=pd.read_csv(f"{nombre.csv}"")
  nombre=nombre.drop(columns='Unnamed: 0',axis=1)
  return nombre

funcion_categoria(d3)

with st.sidebar:
  st.header('Categorias')
  cate_opciones=["3D", "Arte", "Audio","Asistente de Código"]
  choice = st.selectbox("",cate_opciones)

  if choice=='3D':
    if choice=='3D':
    for i in range(len(d3)):
          st.write(f"{[d3.iloc[i][0]]}(%s)" % d3.iloc[i][2])
          st.caption(d3.iloc[i][1])

    
    #for i in range(len(df_3d)):
    #      st.write(f"{[df_3d.iloc[i][0]]}(%s)" % df_3d.iloc[i][2])
    #      st.caption(df_3d.iloc[i][1])
          
  elif choice=='Arte':
    for i in range(len(art)):
          st.write(f"{[art.iloc[i][0]]}(%s)" % art.iloc[i][2])
          st.caption(art.iloc[i][1])

  elif choice=='Audio':
    for i in range(len(Audio)):
          st.write(f"{[Audio.iloc[i][0]]}(%s)" % Audio.iloc[i][2])
          st.caption(Audio.iloc[i][1])

  elif choice=='Asistente de Código':
    for i in range(len(code_assistant)):
          st.write(f"{[code_assistant.iloc[i][0]]}(%s)" % code_assistant.iloc[i][2])
          st.caption(code_assistant.iloc[i][1])            



