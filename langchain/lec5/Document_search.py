from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

document = [
    "Virat kohli is greatest batsaman",
    "Jasprit Bumrah is greatest bowler"
]

query = "Tell me about Bumrah"

vector = embedding.embed_documents(document)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding],vector)[0]
print(document[sorted(list(enumerate(scores)),key=lambda x:x[1])[-1][0]])

