from dotenv import load_dotenv
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

load_dotenv()

pdf_path = Path("__file__").parent/"nodejs.pdf"

#load this pdf in python using langchain

loader = PyPDFLoader(file_path=pdf_path)
docs = loader.load()


#Chunk the document into smaller pieces using langchain text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400)

chunks = text_splitter.split_documents(documents=docs)


#vectorize the chunks using langchain's vectorizer(Vector Embeddings)
embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

#store the vectorized chunks in a vector database (Qdrant) using langchain's vector store interface
vector_store = QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="pdf_rag"
)

print("Indexing of the document is done...")