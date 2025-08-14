# 🤖 FAQ Chatbot sobre Python com Agno e OpenAI

Este projeto implementa um chatbot inteligente de perguntas frequentes sobre Python, utilizando a biblioteca **Agno**, a API da **OpenAI** e uma interface interativa com **Streamlit**.

## 🧠 O que o chatbot faz?

- Responde dúvidas comuns sobre a linguagem Python.
- Mantém o contexto da conversa para interações mais naturais.
- Ideal para iniciantes que desejam aprender conceitos básicos de programação.

## 🛠️ Tecnologias Utilizadas

- Agno: Framework leve para criação de agentes com LLMs.
- OpenAI API: Modelo de linguagem (GPT-3.5).
- Streamlit: Interface web interativa.
- Python-dotenv: Gerenciamento seguro da chave da API.

## 📦 Instalação

    1. Clone o repositório:

        git clone https://github.com/viniciusbertoquintino/AI-Projects/faq-chatbot-agno.git
        cd faq-chatbot-agno

    2 . Instale as dependências:

        pip install -r requirements.txt

    3. Crie um arquivo .env com sua chave da OpenAI:

        OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx