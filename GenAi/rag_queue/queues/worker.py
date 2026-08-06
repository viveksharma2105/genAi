from openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore

openai_client = OpenAI()

embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="pdf_rag",
    embedding=embedding_model
)

def process_query(query: str):
    print("Searching chunks",query)
    search_results = vector_db.similarity_search(query=user_query)
    
    context = "\n\n\n".join([f"Page Content: {result.page_content} \n Page Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}" for result in search_results])
    