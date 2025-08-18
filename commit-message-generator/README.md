# 🤖 Commit Message Generator with AI

This project implements an intelligent tool that analyzes code changes and automatically generates Git commit messages using OpenAI's language model.

## 🧠 What it does

- Reads code modifications using Git.
- Sends the diff to OpenAI's API.
- Returns a concise and contextual commit message suggestion.

## 🛠️ Technologies Used

- Python
- GitPython
- OpenAI API
- python-dotenv

## 📦 Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/viniciusbertoquintino/AI-Projects/commit-message-generator.git
    cd commit-message-generator

2 . Install dependencies:

    pip install -r requirements.txt

3. Create a .env file with your OpenAI API key:

    OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

🚀 Usage
Run the tool to analyze your current Git changes and generate a commit message:

    python main.py

📁 Project Structure
commit-message-generator/
├── main.py                 # Main script
├── analyzer.py             # Git diff analyzer
├── generator.py            # Commit message generator using OpenAI
├── requirements.txt        # Dependencies
├── .env                    # API key
├── README.md               # Documentation

✨ Goal
This project helps developers maintain clean and consistent commit messages effortlessly using AI.