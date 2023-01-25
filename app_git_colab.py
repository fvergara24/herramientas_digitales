
import streamlit as st

st.set_page_config(page_title='Herramientas digitales en español')
st.title('Empoweringrace')

st.title('Herramientas digitales en español')
st.title('dataframe')

!pip install BeautifulSoup

import pandas as pd
from bs4 import BeautifulSoup
import requests
from textblob import TextBlob

url = 'https://www.futurepedia.io/?filter=Free+Trial'
response = requests.get(url)
html  = response.content
scraped = BeautifulSoup(html,'html.parser')
soup = BeautifulSoup(response.text,'html.parser')

a_todos=soup.find_all('h3', class_='MuiTypography-root MuiTypography-h6 MuiTypography-alignLeft css-1xoyy38')
nombres=[]
for element in a_todos:
  nombres.append(element.text)


#url=soup.find_all()
#url_lista=[]
#for element in url_lista:
#  url_lista.append(element.text)

elements=soup.find_all('p', class_='MuiTypography-root MuiTypography-body1 MuiTypography-alignLeft ellipsis css-s2j11')
describes=[]
for element in elements:
  describes.append(element.text)

descripcion_español=[]
for i in range(len(describes)):
  oracion=describes[i]
  o=TextBlob(oracion)
  o_traduccion=o.translate(from_lang='en', to='es')
  descripcion_español.append(str(o_traduccion))

votados=soup.find_all('div', style='display:flex;justify-content:space-between;align-items:center')
votos=[]
for i in range(len(votados)):
  votos.append(votados[i]['aria-label'].split(' ')[0])

dicc={'Nombres':nombres,'Descripcion':descripcion_español,'Votos':votos}
df = pd.DataFrame(dicc)
df['Nombres'][0]=df['Nombres'][0].split('.')[0]
df['Votos']=df['Votos'].astype('int')

st.dataframe(df)
