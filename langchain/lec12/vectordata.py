from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from langchain_chroma import Chroma
from langchain.schema import Document
from chromadb.utils import embedding_functions


embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

default_fun = embedding_functions.DefaultEmbeddingFunction()


doc1 = Document(
    page_content= "Virat kohli is greatest batsaman ",
    metadata = {"team":"Roayal challengers Bengalore"}
)
doc2 = Document(
    page_content= "Jasprit Bumrah is greatest bowler",
    metadata = {"team":"Mumbai Indians"}
)

docs = [doc1,doc2]

vector_database = Chroma(
    embedding_function = embedding,
    persist_directory= 'Chroma_db',
    collection_name = "Sample"
)

print(vector_database.add_documents(docs))

print(vector_database.get(include=['embeddings','documents','metadatas']))

print(vector_database.similarity_search(query="Who is a batsman?"))

print(vector_database.similarity_search_with_score(query="Who is a batsman?"))

updated_Vrecord = Document(
    page_content="Virat Is known for his aggressive batting and captancy.",
    metadata = {'team':'RCB'}
)

print(vector_database.update_document(document_id='4365f969-4395-4f63-95e0-d321c8553fe9',document=updated_Vrecord))

print(vector_database.get(include=['documents','metadatas']))
vector_database.delete_collection()