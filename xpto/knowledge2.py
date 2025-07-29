from agno.agent import Agent
from agno.knowledge.pdf import PDFKnowledgeBase
from agno.vectordb.mongodb import MongoDb
from agno.document.chunking.agentic import AgenticChunking
from agno.embedder.google import GeminiEmbedder
from dotenv import load_dotenv
load_dotenv()

# MongoDB Atlas connection string
"""
Example connection strings:
"mongodb+srv://<username>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority"
"mongodb://localhost/?directConnection=true"
"""
mdb_connection_string = ""

pdf_knowledge_base = PDFKnowledgeBase(
    path="data/pdfs",
    # Collection name: pdf_documents
    vector_db=MongoDb(
        collection_name="pdf_documents",
        db_url=mdb_connection_string,
        wait_until_index_ready=60,
        wait_after_insert=300,
        embedder=GeminiEmbedder(api_key="google_api_key"),
    ),
    chunking_strategy=AgenticChunking(),
)

pdf_knowledge_base.load(recreate=True) # Uncomment to recreate the knowledge base

agent = Agent(knowledge=pdf_knowledge_base, show_tool_calls=True)
agent.print_response("How to make Thai curry?", markdown=True)