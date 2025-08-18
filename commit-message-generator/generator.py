import os
import openai
from dotenv import load_dotenv

# Carregar chave da API
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_commit_message(diff_text: str) -> str:
    prompt = (
        "You are an assistant that writes concise and clear Git commit messages.\n"
        "Given the following code changes (diff), generate a commit message that summarizes the changes:\n\n"
        f"{diff_text}\n\n"
        "Commit message:"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that writes Git commit messages."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=100
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Erro ao gerar mensagem de commit: {e}"
