
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
education_asistant=pd.read_csv('education_assitant.csv')
education_asistant=education_asistant.drop(columns='Unnamed: 0',axis=1)
email_assitant=pd.read_csv('email_assitant.csv')
email_assitant=email_assitant.drop(columns='Unnamed: 0',axis=1)

experiments=pd.read_csv('experiments.csv')
experiments=experiments.drop(columns='Unnamed: 0',axis=1)

fashion_assistant=pd.read_csv('fashion_assistant.csv')
fashion_assistant=fashion_assistant.drop(columns='Unnamed: 0',axis=1)

finance=pd.read_csv('finance.csv')
finance=finance.drop(columns='Unnamed: 0',axis=1)
fun_tools=pd.read_csv('fun_tools.csv')
fun_tools=fun_tools.drop(columns='Unnamed: 0',axis=1)
gaming=pd.read_csv('gaming.csv')
gaming=gaming.drop(columns='Unnamed: 0',axis=1)
general_writing=pd.read_csv('general_writing.csv')
general_writing=general_writing.drop(columns='Unnamed: 0',axis=1)
gift_ideas=pd.read_csv('gift_ideas.csv')
gift_ideas=gift_ideas.drop(columns='Unnamed: 0',axis=1)
healtcare=pd.read_csv('healthcare.csv')
healtcare=healtcare.drop(columns='Unnamed: 0',axis=1)
human_resources=pd.read_csv('human_resources.csv')
human_resources=human_resources.drop(columns='Unnamed: 0',axis=1)
image_editing=pd.read_csv('image_editing.csv')
image_editing=image_editing.drop(columns='Unnamed: 0',axis=1)
image_generator=pd.read_csv('image_generator.csv')
image_generator=image_generator.drop(columns='Unnamed: 0',axis=1)
legal_assistant=pd.read_csv('legal_assistant.csv')
legal_assistant=legal_assistant.drop(columns='Unnamed: 0',axis=1)
logo_generator=pd.read_csv('logo_generator.csv')
logo_generator=logo_generator.drop(columns='Unnamed: 0',axis=1)
low_code_no_code=pd.read_csv('low_code_no_code.csv')
low_code_no_code=low_code_no_code.drop(columns='Unnamed: 0',axis=1)
memory_assistant=pd.read_csv('memory_assistant.csv')
memory_assistant=memory_assistant.drop(columns='Unnamed: 0',axis=1)
music_generator=pd.read_csv('music_generator.csv')
music_generator=music_generator.drop(columns='Unnamed: 0',axis=1)
paraphraser=pd.read_csv('paraphraser.csv')
paraphraser=paraphraser.drop(columns='Unnamed: 0',axis=1)
personalized_videos=pd.read_csv('personalized_videos.csv')
personalized_videos=personalized_videos.drop(columns='Unnamed: 0',axis=1)
presentation=pd.read_csv('presentations.csv')
presentation=presentation.drop(columns='Unnamed: 0',axis=1)
productivity=pd.read_csv('productivity.csv')
productivity=productivity.drop(columns='Unnamed: 0',axis=1)
prompts=pd.read_csv('prompts.csv')
prompts=prompts.drop(columns='Unnamed: 0',axis=1)
real_state=pd.read_csv('real_estate.csv')
real_state=real_state.drop(columns='Unnamed: 0',axis=1)
research=pd.read_csv('research.csv')
research=research.drop(columns='Unnamed: 0',axis=1)
resources=pd.read_csv('resources.csv')
resources=resources.drop(columns='Unnamed: 0',axis=1)
sales=pd.read_csv('sales.csv')
sales=sales.drop(columns='Unnamed: 0',axis=1)
search_engine=pd.read_csv('search_engine.csv')
search_engine=search_engine.drop(columns='Unnamed: 0',axis=1)
seo=pd.read_csv('seo.csv')
seo=seo.drop(columns='Unnamed: 0',axis=1)
social_media_assistant=pd.read_csv('social_media_assistant.csv')
social_media_assistant=social_media_assistant.drop(columns='Unnamed: 0',axis=1)
spreadsheet=pd.read_csv('spreadsheet.csv')
spreadsheet=spreadsheet.drop(columns='Unnamed: 0',axis=1)
sql=pd.read_csv('sql.csv')
sql=sql.drop(columns='Unnamed: 0',axis=1)
startup_tools=pd.read_csv('startup_tools.csv')
startup_tools=startup_tools.drop(columns='Unnamed: 0',axis=1)
storyteller=pd.read_csv('storyteller.csv')
storyteller=storyteller.drop(columns='Unnamed: 0',axis=1)
summarizer=pd.read_csv('summarizer.csv')
summarizer=summarizer.drop(columns='Unnamed: 0',axis=1)
text_to_speech=pd.read_csv('text_to_speech.csv')
text_to_speech=text_to_speech.drop(columns='Unnamed: 0',axis=1)
transcriber=pd.read_csv('transcriber.csv')
transcriber=transcriber.drop(columns='Unnamed: 0',axis=1)
video_editing=pd.read_csv('video_editing.csv')
video_editing=video_editing.drop(columns='Unnamed: 0',axis=1)
video_generator=pd.read_csv('video_generator.csv')
video_generator=video_generator.drop(columns='Unnamed: 0',axis=1)


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
                "Educación",
                "Email",
                "Experimentos",
                "Asistente de moda",
                "Finanzas",
                "Herramientas divertidas",
                "Juegos",
                "Escritura en general",
                "Ideas gift",
                "Salud",
                "Recursos humanos",
                "Edición de imágenes",
                "Generador de imágenes",
                "Asistencia legal",
                "Generación del logo",
                "Sin código",
                "Asistente de memoria",
                "Generador de música",
                "Paráfrasis",
                "Videos personalizados",
                "Presentaciones",
                "Productividad",
                "Indicaciones para Inteligencia Artificial",
                "Inmobiliaria",
                "Requerimientos",
                "Búsqueda",
                "Ventas",
                "Motor de búsqueda",
                "SEO",
                "Redes sociales",
                "Hojas de cálculo",
                "SQL",
                "Herramientas de Startup",
                "Storyteller",
                "Resumen",
                "Texto para hablar",
                "Transcibir",
                "Edición de video",
                "Generador de video"]
  
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

  elif choice=='Educación':
    for i in range(len(education_asistant)):
          st.write(f"{[education_asistant.iloc[i][0]]}(%s)" % education_asistant.iloc[i][2])
          st.caption(education_asistant.iloc[i][1]) 
  
  elif choice=='Email':
    for i in range(len(email_assitant)):
          st.write(f"{[email_assitant.iloc[i][0]]}(%s)" % email_assitant.iloc[i][2])
          st.caption(email_assitant.iloc[i][1]) 
          
  elif choice=='Experimentos':
    for i in range(len(experiments)):
          st.write(f"{[experiments.iloc[i][0]]}(%s)" % experiments.iloc[i][2])
          st.caption(experiments.iloc[i][1])
  
  elif choice=='Asistente de moda':
    for i in range(len(fashion_assistant)):
          st.write(f"{[fashion_assistant.iloc[i][0]]}(%s)" % fashion_assistant.iloc[i][2])
          st.caption(fashion_assistant.iloc[i][1])

  elif choice=='Finanzas':
    for i in range(len(finance)):
          st.write(f"{[finance.iloc[i][0]]}(%s)" % finance.iloc[i][2])
          st.caption(finance.iloc[i][1])

  elif choice=='Herramientas divertidas':
    for i in range(len(fun_tools)):
          st.write(f"{[fun_tools.iloc[i][0]]}(%s)" % fun_tools.iloc[i][2])
          st.caption(fun_tools.iloc[i][1])

  elif choice=='Juegos':
    for i in range(len(gaming)):
          st.write(f"{[gaming.iloc[i][0]]}(%s)" % gaming.iloc[i][2])
          st.caption(gaming.iloc[i][1])

  elif choice=='Escritura en general':
    for i in range(len(general_writing)):
          st.write(f"{[general_writing.iloc[i][0]]}(%s)" % general_writing.iloc[i][2])
          st.caption(general_writing.iloc[i][1])

  elif choice=='Ideas gift':
    for i in range(len(gift_ideas)):
          st.write(f"{[gift_ideas.iloc[i][0]]}(%s)" % gift_ideas.iloc[i][2])
          st.caption(gift_ideas.iloc[i][1])

  elif choice=='Salud':
    for i in range(len(healtcare)):
          st.write(f"{[healtcare.iloc[i][0]]}(%s)" % healtcare.iloc[i][2])
          st.caption(healtcare.iloc[i][1])

  elif choice=='Recursos humanos':
    for i in range(len(human_resources)):
          st.write(f"{[human_resources.iloc[i][0]]}(%s)" % human_resources.iloc[i][2])
          st.caption(human_resources.iloc[i][1])

  elif choice=='Edición de imágenes':
    for i in range(len(image_editing)):
          st.write(f"{[image_editing.iloc[i][0]]}(%s)" % image_editing.iloc[i][2])
          st.caption(image_editing.iloc[i][1])

  elif choice=='Generador de imágenes':
    for i in range(len(image_generator)):
          st.write(f"{[image_generator.iloc[i][0]]}(%s)" % image_generator.iloc[i][2])
          st.caption(image_generator.iloc[i][1])

  elif choice=='Asistencia legal':
    for i in range(len(legal_assistant)):
          st.write(f"{[legal_assistant.iloc[i][0]]}(%s)" % legal_assistant.iloc[i][2])
          st.caption(legal_assistant.iloc[i][1])

  elif choice=='Generación del logo':
    for i in range(len(logo_generator)):
          st.write(f"{[logo_generator.iloc[i][0]]}(%s)" % logo_generator.iloc[i][2])
          st.caption(logo_generator.iloc[i][1])

  elif choice=='Sin código':
    for i in range(len(low_code_no_code)):
          st.write(f"{[low_code_no_code.iloc[i][0]]}(%s)" % low_code_no_code.iloc[i][2])
          st.caption(low_code_no_code.iloc[i][1])

  elif choice=='Asistente de memoria':
    for i in range(len(memory_assistant)):
          st.write(f"{[memory_assistant.iloc[i][0]]}(%s)" % memory_assistant.iloc[i][2])
          st.caption(memory_assistant.iloc[i][1])

  elif choice=='Generador de música':
    for i in range(len(music_generator)):
          st.write(f"{[music_generator.iloc[i][0]]}(%s)" % music_generator.iloc[i][2])
          st.caption(music_generator.iloc[i][1])

  elif choice=='Paráfrasis':
    for i in range(len(paraphraser)):
          st.write(f"{[paraphraser.iloc[i][0]]}(%s)" % paraphraser.iloc[i][2])
          st.caption(paraphraser.iloc[i][1])

  elif choice=='Videos personalizados':
    for i in range(len(personalized_videos)):
          st.write(f"{[personalized_videos.iloc[i][0]]}(%s)" % personalized_videos.iloc[i][2])
          st.caption(personalized_videos.iloc[i][1])

  elif choice=='Presentaciones':
    for i in range(len(presentations)):
          st.write(f"{[personapresentationslized_videos.iloc[i][0]]}(%s)" % presentations.iloc[i][2])
          st.caption(presentations.iloc[i][1])

  elif choice=='Productividad':
    for i in range(len(productivity)):
          st.write(f"{[productivity.iloc[i][0]]}(%s)" % productivity.iloc[i][2])
          st.caption(productivity.iloc[i][1])

  elif choice=='Indicaciones para Inteligencia Artificial':
    for i in range(len(prompts)):
          st.write(f"{[prompts.iloc[i][0]]}(%s)" % prompts.iloc[i][2])
          st.caption(prompts.iloc[i][1])

  elif choice=='Inmobiliaria':
    for i in range(len(real_state)):
          st.write(f"{[real_state.iloc[i][0]]}(%s)" % real_state.iloc[i][2])
          st.caption(real_state.iloc[i][1])

  elif choice=='Requerimientos':
    for i in range(len(requirements)):
          st.write(f"{[requirements.iloc[i][0]]}(%s)" % requirements.iloc[i][2])
          st.caption(requirements.iloc[i][1])

  elif choice=='Búsqueda':
    for i in range(len(research)):
          st.write(f"{[research.iloc[i][0]]}(%s)" % research.iloc[i][2])
          st.caption(research.iloc[i][1])

  elif choice=='Ventas':
    for i in range(len(sales)):
          st.write(f"{[sales.iloc[i][0]]}(%s)" % sales.iloc[i][2])
          st.caption(sales.iloc[i][1])

  elif choice=='Motor de búsqueda':
    for i in range(len(resources)):
          st.write(f"{[resources.iloc[i][0]]}(%s)" % resources.iloc[i][2])
          st.caption(resources.iloc[i][1])

@st.cache(allow_output_mutation=True)
def Pageviews():
    return []

pageviews=Pageviews()
pageviews.append('dummy')

try:
    st.markdown('Page viewed = {} times.'.format(len(pageviews)))
except ValueError:
    st.markdown('Page viewed = {} times.'.format(1))

