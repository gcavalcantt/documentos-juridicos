import streamlit as st
import spacy
from spacy_streamlit import visualize_ner

# Configura o título da aplicação Streamlit
st.title('Reconhecimento de entidades nomeadas (NER)')

# Define o caminho do modelo treinado para reconhecimento de entidades
caminho_modelo = 'C:/Users/guilh/Documents/NER-streamlit/modelo'
modelo = spacy.load(caminho_modelo)  # Carrega o modelo de NER treinado

# Obtém os rótulos das entidades do modelo
rotulos = list(modelo.get_pipe('ner').labels)

# Define cores personalizadas para diferentes tipos de entidades
cores = {
    'B-JURISPRUDENCIA': '#F0F8FF',
    'B-LEGISLACAO': '#FA8072',
    'B-LOCAL': '#98FB98',
    'B-ORGANIZACAO': '#DDA0DD',
    'B-PESSOA': '#F0E68C',
    'B-TEMPO': '#FFB6C1',
    'I-JURISPRUDENCIA': '#F0F8FF',
    'I-LEGISLACAO': '#FA8072',
    'I-LOCAL': '#98FB98',
    'I-ORGANIZACAO': '#DDA0DD',
    'I-PESSOA': '#F0E68C',
    'I-TEMPO': '#FFB6C1',
    'LOC': '#D3D3D3',
    'MISC': '#D3D3D3',
    'ORG': '#D3D3D3',
    'PER': '#D3D3D3'
}

# Define opções para a visualização das entidades
opcoes = {'ents': rotulos, 'colors': cores}

# Adiciona um seletor de opções no Streamlit para escolher entrada via texto ou arquivo
escolha = st.radio(label='Escolha uma opção:', options=['Texto', 'Arquivo'])

# Inicializa a variável de texto vazia
texto = ''

# Permite ao usuário inserir texto manualmente
if escolha == 'Texto':
    texto = st.text_area('Insira o texto:')

# Permite ao usuário fazer upload de um arquivo .txt
elif escolha == 'Arquivo':
    arquivo = st.file_uploader('Faça o upload do arquivo (somente .txt):', type='txt')
    if arquivo is not None:
        texto = arquivo.read().decode('utf-8')  # Lê e decodifica o conteúdo do arquivo

# Processa o texto usando o modelo NER
doc = modelo(texto)

# Visualiza as entidades nomeadas identificadas no texto
visualize_ner(
    doc,
    labels=rotulos,
    displacy_options=opcoes,
    title='Reconhecimento de entidades nomeadas'
)