from agno.agent import Agent
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.vectordb.mongodb import MongoDb
from agno.document.chunking.agentic import AgenticChunking
from agno.models.openai import OpenAIChat
# from agno.playground import Playground
from agno.embedder.google import GeminiEmbedder
import os
from dotenv import load_dotenv
load_dotenv()


# String de conexão do MongoDB Atlas ou local
mdb_connection_string = "mongodb://localhost:27017"import pymongo

pdf_knowledge_base = PDFKnowledgeBase(
    path="data/pdfs",
    vector_db=MongoDb(
        collection_name="bulas_pdf",
        db_url=mdb_connection_string,
        embedder=GeminiEmbedder(api_key=os.getenv("API_KEY_GOOGLE")),
    ),
    chunking_strategy=AgenticChunking(),
)

# Apenas descomente na primeira vez para carregar/atualizar os PDFs
pdf_knowledge_base.load(recreate=True)

vini_gui = Agent(knowledge=pdf_knowledge_base, show_tool_calls=True)

print("Agno Playground PDF - Pergunte sobre o conteúdo dos seus PDFs (digite 'sair' para encerrar)\n")
while True:
    pergunta = input("Pergunta: ")
    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("Saindo do playground.")
        break
    print("\nResposta:")
    agent.print_response(pergunta, markdown=True)
    print("-" * 60)

# playground_app = Playground(agents=vini_gui, title="Agno Playground PDF")
# app = playground_app.get_app()

# if __name__ == "__main__":
    # playground_app.serve("playground:app", reload=True)