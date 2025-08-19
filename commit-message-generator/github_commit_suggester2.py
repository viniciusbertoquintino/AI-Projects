import os
from github import Github
from dotenv import load_dotenv
from groq import Groq

# Carregar variáveis de ambiente
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Validar tokens
if not GITHUB_TOKEN or not GROQ_API_KEY:
    raise ValueError("GITHUB_TOKEN ou GROQ_API_KEY não encontrados. Verifique o arquivo .env.")

# Inicializar clientes
g = Github(GITHUB_TOKEN)
client = Groq(api_key=GROQ_API_KEY)

# Nome do repositório
repo_name = "viniciusbertoquintino/AI-Projects"

try:
    # Acessar o repositório
    repo = g.get_repo(repo_name)

    # Obter o último commit da branch principal
    branch = repo.get_branch("main")
    latest_commit_sha = branch.commit.sha
    latest_commit = repo.get_commit(latest_commit_sha)

    # Obter arquivos modificados
    modified_files = [file.filename for file in latest_commit.files]
    diff_summary = "\n".join([
        f"{file.filename}: {file.patch[:300]}..." 
        for file in latest_commit.files if file.patch
    ])

    # Gerar sugestão de mensagem de commit com Groq
    prompt = (
        "Você é um assistente que escreve mensagens de commit claras e concisas no estilo Conventional Commits.\n"
        "Com base nas seguintes modificações de código, gere uma sugestão de mensagem de commit:\n\n"
        f"{diff_summary}\n\nMensagem de commit:"
    )

    response = client.chat.completions.create(
        model="llama3-8b-8192",  # ou "mixtral-8x7b-32768"
        messages=[
            {"role": "system", "content": "Você é um assistente útil que escreve mensagens de commit para desenvolvedores."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.5,
        max_tokens=100
    )

    commit_message = response.choices[0].message.content.strip()

    # Exibir resultado
    print("Arquivos modificados no último commit:")
    print("\n".join(modified_files))
    print("\nSugestão de mensagem de commit:")
    print(commit_message)

except Exception as e:
    print(f"Erro durante execução: {e}")
