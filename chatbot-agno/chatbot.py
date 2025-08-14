import os
from agno import Agent
from dotenv import load_dotenv

# Carregar chave da API do arquivo .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Definir o prompt base do assistente
faq_prompt = """
Você é um assistente inteligente que responde perguntas frequentes sobre Python.
Seja claro, direto e amigável. Mantenha o contexto da conversa e ajude iniciantes a entenderem conceitos básicos.
"""

# Criar o agente com Agno
faq_bot = Agent(
    prompt=faq_prompt,
    provider="openai:gpt-3.5-turbo",
    api_key=openai_api_key,
    memory=True,
    stream=False
)

# Função para responder perguntas
def responder_pergunta(pergunta: str) -> str:
    resposta = faq_bot.ask(pergunta)
    return resposta
