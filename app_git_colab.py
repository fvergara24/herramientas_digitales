
import streamlit as st
import pandas as pd

st.set_page_config(page_title='Herramientas digitales en español', page_icon='favicon.jpg')
# st.write('↖ Categorias')
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
d3=pd.read_csv('d3.csv')
d3=d3.drop(columns='Unnamed: 0',axis=1)
art=pd.read_csv('art.csv')
art=art.drop(columns='Unnamed: 0',axis=1)
Audio=pd.read_csv('audio.csv')
Audio=Audio.drop(columns='Unnamed: 0',axis=1)
code_assistant=pd.read_csv('code_assistant.csv')
code_assistant=code_assistant.drop(columns='Unnamed: 0',axis=1)
copywriting=pd.read_csv('copywriting.csv')
copywriting=copywriting.drop(columns='Unnamed: 0',axis=1)
customer_support=pd.read_csv('customer_support.csv')
customer_support=customer_support.drop(columns='Unnamed: 0',axis=1)
design_assitant=pd.read_csv('design_assitant.csv')
design_assitant=design_assitant.drop(columns='Unnamed: 0',axis=1)
developer_tools=pd.read_csv('developer_tools.csv')
developer_tools=developer_tools.drop(columns='Unnamed: 0',axis=1)
e_commerce=pd.read_csv('e_commerce.csv')
e_commerce=e_commerce.drop(columns='Unnamed: 0',axis=1)




with st.sidebar:
  st.header('Categorias')
  cate_opciones=["3D", 
                "Arte", 
                "Audio",
                "Asistente de Código",
                "Redacción",
                "Soporte al Cliente",
                "Asistente de Diseño",
                "Herramientas de Desarrollador",
                "Comercio Electrónico",
                  ]
  choice = st.selectbox("",cate_opciones)

  if choice=='3D':
    for i in range(len(d3)):
          st.write(f"{[d3.iloc[i][0]]}(%s)" % d3.iloc[i][2])
          st.caption(d3.iloc[i][1])
          
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

  elif choice=='Redacción':
    for i in range(len(copywriting)):
          st.write(f"{[copywriting.iloc[i][0]]}(%s)" % copywriting.iloc[i][2])
          st.caption(copywriting.iloc[i][1]) 

  elif choice=='Soporte al Cliente':
    for i in range(len(customer_support)):
          st.write(f"{[customer_support.iloc[i][0]]}(%s)" % customer_support.iloc[i][2])
          st.caption(customer_support.iloc[i][1]) 

  elif choice=='Asistente de Diseño':
    for i in range(len(design_assitant)):
          st.write(f"{[design_assitant.iloc[i][0]]}(%s)" % design_assitant.iloc[i][2])
          st.caption(design_assitant.iloc[i][1]) 

  elif choice=='Herramientas de Desarrollador':
    for i in range(len(developer_tools)):
          st.write(f"{[developer_tools.iloc[i][0]]}(%s)" % developer_tools.iloc[i][2])
          st.caption(developer_tools.iloc[i][1]) 

  elif choice=='Comercio Electrónico':
    for i in range(len(e_commerce)):
          st.write(f"{[e_commerce.iloc[i][0]]}(%s)" % e_commerce.iloc[i][2])
          st.caption(e_commerce.iloc[i][1])         


