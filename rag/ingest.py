from pathlib import Path

from langchain_core.documents import Document

from langchain_chroma import Chroma

from langchain_mistralai import MistralAIEmbeddings

docs = []

data_dir = Path("data")

for file in data_dir.rglob("*.txt"):

    text = file.read_text(
        encoding="utf-8"
    )

    docs.append(
        Document(
            page_content=text
        )
    )

embedding = MistralAIEmbeddings(
    model="mistral-embed"
)

Chroma.from_documents(
    docs,
    embedding,
    persist_directory="./vectorstore"
)

print("Done")