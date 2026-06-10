from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from openai import OpenAI

load_dotenv()
openai_client = OpenAI()


embedding_model = OpenAIEmbeddings(
    model="text-embedding-3-large"
)

vector_db = QdrantVectorStore.from_existing_collection(
    url="http://localhost:6333",
    collection_name="pdf_rag",
    embedding=embedding_model
)

#Take user Input
user_query = input("Ask something...: ")

#Relevant chunks from the vectorDB
search_results = vector_db.similarity_search(query=user_query)


context = "\n\n\n".join([f"Page Content: {result.page_content} \n Page Number: {result.metadata['page_label']}\nFile Location: {result.metadata['source']}" for result in search_results])

SYSTEM_PROMPT = f"""
You are a helpful assistant who answers user query based on the available context retrived from a pdf file along with the page_contents and page number(must).

You should only answer the question based on the available context and not make up any answer if the answer is not present in the context. 

context: {context}
"""

response = openai_client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query}
    ]
)

print(f"🤖: {response.choices[0].message.content}")