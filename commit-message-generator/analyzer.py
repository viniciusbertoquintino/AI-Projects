import git

def get_git_diff():
    try:
        repo = git.Repo(".")
        diff_text = ""
        for item in repo.index.diff(None):
            try:
                diff_text += repo.git.diff(item.a_path) + "\n"
            except Exception as e:
                diff_text += f"Erro ao obter diff de {item.a_path}: {e}\n"
        return diff_text
    except Exception as e:
        return f"Erro ao acessar o repositório Git: {e}"
