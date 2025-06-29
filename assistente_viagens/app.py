import os
from dotenv import load_dotenv
load_dotenv() # Le o arquivo .env, a chave da open IA deve estar la porem nesse exemplo esta em um arquivo separado

from langchain_openai import ChatOpenAI # Importa o modelo de linguagem da OpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder # Importa o template de prompt para o chat, ja o mesages placeholder e usado para armazenar as mensagens do chat
from langchain_core.runnables.history import RunnableWithMessageHistory # Importa o histórico de mensagens para manter o contexto da conversa
from langchain_core.chat_history import BaseChatMessageHistory # Importa a classe base para o histórico de mensagens do chat
from langchain_community.chat_message_histories import ChatMessageHistory # Importa a implementação do histórico de mensagens para o chat

template = """Você é um assistente de viagens que ajuda o usuario a planejar viagen, dando sugestões de destinos, roteiros e dicas praticas. " \
A primeira coisa que voce deve fazer é perguntar para onde o usuario vai, com quantas pessoas e por quanto tempo

Historico da conversa: 
{history}

Entrada do usuario:
{input}"""

prompt = ChatPromptTemplate.from_messages([
    ("system", template),  # Define o template do sistema
    MessagesPlaceholder(variable_name="history"),  # Placeholder para o histórico de mensagens
    ("human", "{input}")  # Entrada do usuário
])