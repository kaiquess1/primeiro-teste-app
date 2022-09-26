import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import pydeck as pdk
import pickle
import seaborn as sns
import matplotlib.pyplot as plt
#imagem=Image.open('page-icon.png')
st.set_page_config(page_title='Angola 2022', page_icon='https://i.pinimg.com/originals/be/0e/7a/be0e7a66443ef7c46b061f1de1ec4574.png')
#Aqui estou confirgurando apresentaçao do site, como o nome e icone que vai aparecer ao abrir a pagina.
st.write('# Monkeypox')
st.markdown('Acompanhando a evolução da doença pelo mundo')
st.write('-----------')
st.sidebar.write('Periodo')
data=pd.read_csv("./venv/monkeypox.csv")
label=list(['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro'])
meses=st.sidebar.selectbox('Escolha o periodo',options=label)
#Aqui estou criando uma caixa para selecionar o mes que desejo verificar as informações

data['Date_confirmation']=pd.to_datetime(data['Date_confirmation'])
data['month']=data['Date_confirmation'].dt.strftime('%m')
mes=(data['month'].unique())
inicia_mes=int(mes.min())
final_mes=int(mes.max())

periodo=st.sidebar.slider('Escolha um mês',min_value=inicia_mes,max_value=final_mes,value=final_mes)
#Aqui estou criando uma linha para filtrar o periodo que desejo obter as informações.
#Vale ressaltar que para obter a interação tive que salvar o comando em uma variavél PERIODO
st.sidebar.write('O mes escolhido foi:',periodo)


if meses == 'Fevereiro':
    st.write('# Carnaval binho')
if meses=='Maio':
    st.write(' # Ano que vem be')
if meses == 'Julho':
    st.write('# Vem sao jao')
#Aqui estou interagindo com o selectbox as opções escolhidas

if st.sidebar.checkbox('Mostrar tabela'):
    st.write(data)
#Aqui estou interagindo com a caixinha do checkbox para apresentar a tabela quando a opção estiver selecionada






