from langchain_community.retrievers import WikipediaRetriever

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.schema import Document
from langchain_community.vectorstores import FAISS

#  WikiPedia retriver 
# retriver = WikipediaRetriever(top_k_results=2, lang="en")

# query = "geopolitical history of india and pakistan from perspective of chinese"

# docs = retriver.invoke(query)

# for i, doc in enumerate(docs):
#     print("-"*20+f"Result {i} "+"-"*20)
#     print(doc.page_content)




embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')


doc1 = Document(
    page_content= "Virat kohli is greatest batsaman ",
    metadata = {"team":"Roayal challengers Bengalore"}
)
doc2 = Document(
    page_content= "Jasprit Bumrah is greatest bowler",
    metadata = {"team":"Mumbai Indians"}
)

docs = [doc1,doc2]

# vector_database = Chroma(
#     embedding_function = embedding,
#     persist_directory= 'Chroma_db',
#     collection_name = "Sample"
# )

# vector_database = Chroma.from_documents(
#     documents=docs,
#     embedding=embedding,
#     collection_name="Learn_Retrivers"
# )
vector_database = FAISS.from_documents(
    documents=docs,
    embedding=embedding
)

retriver = vector_database.as_retriever(search_type= "mmr",search_kwargs = {'k':1,'lambda': 1})

query = "Who is Virat?"
result = retriver.invoke(query)

for i, doc in enumerate(result):
    print("-"*20+f"Result {i} "+"-"*20)
    print(doc.page_content)
