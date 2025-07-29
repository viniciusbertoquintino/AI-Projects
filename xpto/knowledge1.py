from agno.knowledge.pdf import PDFKnowledgeBase
from agno.vectordb.pgvector import PgVector
from agno.agent import Agent
from agno.document.chunking.agentic import AgenticChunking
from agno.embedder.google import GeminiEmbedder
from dotenv import load_dotenv
load_dotenv()

pdf_knowledge_base = PDFKnowledgeBase(
    path="data/pdfs",
    # Table name: ai.pdf_documents
    vector_db=PgVector(
        table_name="pdf_documents",
        db_url="postgresql+psycopg://ai:ai@localhost:5532/ai",
         embedder=GeminiEmbedder(api_key="google_api_key")
    ),
    chunking_strategy=AgenticChunking(),
)