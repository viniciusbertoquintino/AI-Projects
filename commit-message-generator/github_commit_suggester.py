import os
from github import Github
from dotenv import load_dotenv
import openai

# Carregar variáveis de ambiente
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Inicializar clientes
g = Github(GITHUB_TOKEN)
openai.api_key = OPENAI_API_KEY

# Nome do repositório
repo_name = "viniciusbertoquintino/AI-Projects"

# Acessar o repositório
repo = g.get_repo(repo_name)

# Obter o último commit da branch principal
branch = repo.get_branch("main")
latest_commit_sha = branch.commit.sha
latest_commit = repo.get_commit(latest_commit_sha)

# Obter arquivos modificados
modified_files = [file.filename for file in latest_commit.files]
diff_summary = "\n".join([f"{file.filename}: {file.patch}" for file in latest_commit.files if file.patch])

# Gerar sugestão de mensagem de commit com OpenAI
prompt = (
    "Você é um assistente que escreve mensagens de commit claras e concisas.\n"
    "Com base nas seguintes modificações de código, gere uma sugestão de mensagem de commit:\n\n"
    f"{diff_summary}\n\nMensagem de commit:"
)

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Você é um assistente útil que escreve mensagens de commit para desenvolvedores."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.5,
    max_tokens=100
)

# Exibir resultado
commit_message = response.choices[0].message.content.strip()
print("Arquivos modificados no último commit:")
print("\n".join(modified_files))
print("\nSugestão de mensagem de commit:")
print(commit_message)
