import streamlit as st
from agno import ChatLLM
import os
from dotenv import load_dotenv

# Carregar chave da API do OpenAI
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Inicializar o chatbot com Agno
chatbot = ChatLLM(
    provider="openai",
    model="gpt-3.5-turbo",
    api_key=openai_api_key,
    system_message=(
        "Você é um assistente especializado em responder dúvidas sobre Python. "
        "Seja claro, objetivo e forneça exemplos sempre que possível."
    )
)

# Interface Streamlit
st.set_page_config(page_title="FAQ Chatbot - Python", page_icon="🐍")
st.title("🐍 FAQ Chatbot sobre Python")
st.write("Digite sua dúvida sobre Python e receba uma resposta inteligente!")

# Histórico de mensagens
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar histórico
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Entrada do usuário
user_input = st.chat_input("Digite sua pergunta aqui...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    response = chatbot.ask(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
