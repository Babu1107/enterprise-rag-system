from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores.utils import DistanceStrategy
from langchain_community.embeddings import HuggingFaceEmbeddings

from config import (
  PDF_PATH,
  CHUNK_SIZE,
  CHUNK_OVERLAP,
  EMBEDDING_MODEL
)

docs = PyPDFLoader(PDF_PATH).load()

splitters = RecursiveCharacterTextSplitter(
    chunk_size = CHUNK_SIZE,
    chunk_overlap = CHUNK_OVERLAP
)

final_docs = splitters.split_documents(docs)

embedding_models = HuggingFaceEmbeddings(
    model_name = EMBEDDING_MODEL
)

db = FAISS.from_documents(final_docs, embedding_models, distance_strategy = DistanceStrategy.COSINE)
