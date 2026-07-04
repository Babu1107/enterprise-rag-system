import os
from groq import Groq
from google.colab import userdata

client = Groq(api_key=os.environ["GROQ_API_KEY"])
MODEL_NAME = "openai/gpt-oss-120b"
EMBEDDING_MODEL = "all-MiniLm-L6-v2"
PDF_PATH = "/content/enterprise-rag-system/data/Employee-Travel-Policy.pdf"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
TOP_K = 5
RERANK_THRESHOLD = 0.5