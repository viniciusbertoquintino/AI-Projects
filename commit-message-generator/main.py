from analyzer import get_git_diff
from generator import generate_commit_message

def main():
    print("🔍 Analisando modificações no repositório Git...")
    diff_text = get_git_diff()

    if not diff_text.strip():
        print("✅ Nenhuma modificação detectada.")
        return

    print("\n🧠 Gerando sugestão de mensagem de commit com IA...\n")
    commit_message = generate_commit_message(diff_text)

    print("💬 Sugestão de commit:")
    print("----------------------")
    print(commit_message)
    print("----------------------")

if __name__ == "__main__":
    main()
