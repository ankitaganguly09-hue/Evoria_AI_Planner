from langchain_chroma import Chroma
from langchain_mistralai import MistralAIEmbeddings

embedding = MistralAIEmbeddings(
    model="mistral-embed"
)

db = Chroma(
    persist_directory="./vectorstore",
    embedding_function=embedding
)

retriever = db.as_retriever(
    search_kwargs={"k": 5}
)