from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.embedder.openai import OpenAIEmbedder
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.knowledge.pdf import PDFKnowledgeBase, PDFReader
from agno.playground import Playground, serve_playground_app
from dotenv import load_dotenv
import os
import openai
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

agent_slip = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions="""You are a passionate and knowledgeable AI assistant who can answer questions about medication leaflets. Your responses should be informative and well-researched. Please provide detailed explanations for your answers. If you do not have enough information to answer the question, say so and ask for more details. Always advise the user to consult a doctor.""",
    knowledge=PDFKnowledgeBase(
        path="data",
        vector_db=LanceDb(
            uri="tmp/lancedb",
            table_name="bulas",
            search_type=SearchType.hybrid,
            embedder=OpenAIEmbedder(),
          ),
    reader=PDFReader(chunk=True),
     # chunking_strategy=AgenticChunking(),
),
    show_tool_calls=True,
    markdown=True,
    add_references=True, 
)

if agent_slip.knowledge is not None:
    agent_slip.knowledge.load()

print("Agno Playground PDF - Pergunte sobre o conteúdo dos seus PDFs (digite 'sair' para encerrar)\n")
while True:
    pergunta = input("Pergunta: ")
    if pergunta.lower() in ["sair", "exit", "quit"]:
        print("Saindo do playground.")
        break
    print("\nResposta:")
    agent_slip.print_response(pergunta, markdown=True)
    print("-" * 60)

# Playground Agno

# app = Playground(
    #agents = [
        #agent_slip,
    #] 
# ).get_app(use_async=True)

# if __name__ == "__main__":
    # serve_playground_app("main3:app", reload=True)