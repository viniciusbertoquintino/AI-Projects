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

llm = ChatOpenAI(temperature=0.7,model="gpt-4o-mini")  # Cria uma instância do modelo de linguagem com temperatura ajustada sendo 0.7 e modelo especificado como gpt-4o-mini.

chain = prompt | llm  # Cria uma cadeia de execução que combina o template do prompt com o modelo de linguagem

store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    """Retorna o histórico de mensagens para uma sessão específica."""
    if session_id not in store:
        store[session_id] = ChatMessageHistory()  # Cria um novo histórico se não existir
    return store[session_id]

chain_with_history = RunnableWithMessageHistory(
    chain, 
    get_session_history, # Função para obter o histórico de mensagens da sessão
    input_messages_key="input",  # Define a chave para as mensagens de entrada
    history_messages_key="history"  # Define a chave para as mensagens de histórico
)

def iniciar_assistente_viagem():
    print("Bem-vindo ao Assistente de Viagens! Digite 'Sair' para encerrar a conversa.\n")
    while True:
        pergunta_usuario = input("Você: ")

        if pergunta_usuario.lower() in ["sair", "exit"]:
            print("Assistente de Viagem: Até mais! Aproveite sua viagem!")
            break

        resposta = chain_with_history.invoke(
            {"input": pergunta_usuario},
            config={'configurable': {'session_id': 'user123'}}  # Exemplo de ID de sessão, pode ser dinâmico
        )

        print("Assistente de viagem:", resposta.content)

if __name__ == "__main__":
    iniciar_assistente_viagem()  # Inicia o assistente de viagem