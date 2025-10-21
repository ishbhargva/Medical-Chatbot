from dotenv import load_dotenv
import os
from pinecone import Pinecone
from pinecone import ServerlessSpec 
from langchain_pinecone import PineconeVectorStore

pinecone_api_key = os.getenv('pinecone_api_key')
openai_api_key = os.getenv('openai_api_key')


load_dotenv()

os.environ['PINECONE_API_KEY'] = pinecone_api_key
os.environ['OPENAI_API_KEY'] = openai_api_key



pinecone_api_key = pinecone_api_key

pc = Pinecone(api_key=pinecone_api_key)

index_name = "medical-chatbot"

if not pc.has_index(index_name):
    pc.create_index(
        name = index_name,
        dimension=384,  # Dimension of the embeddings
        metric= "cosine",  # Cosine similarity
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )


index = pc.Index(index_name)

# Load Existing index 
# Embed each chunk and upsert the embeddings into your Pinecone index.
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embedding
)