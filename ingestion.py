from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

from config import EMBEDDING_MODEL

print("Loading FAISS Index...")

embeddings = HuggingFaceEmbeddings(
    model_name=EMBEDDING_MODEL
)

db = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

print("FAISS Loaded Successfully!")