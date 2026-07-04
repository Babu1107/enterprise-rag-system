import json
from state import MyState

from config import (
  client,
  MODEL_NAME,
  TOP_K,
  RERANK_THRESHOLD
)

from prompts import RERANK_PROMPT, GENERATE_PROMPT

from ingestion import db

def rerank_chunks(query, chunks):
  prompt = RERANK_PROMPT.format(
      query = query,
      chunks = chunks
  )

  response = client.chat.completions.create(
      model = MODEL_NAME,
      messages = [{"role":"user", "content":prompt}]
  )

  try:
    scores = json.loads(response.choices[0].message.content)
  except:
    scores = [0] * len(chunks)

  scored = list(zip(chunks, scores))

  scored.sort(key = lambda x:x[1], reverse = True)

  return scored

def retrieve(state:MyState):
  query = state["query"]

  docs = db.similarity_search_with_score(query, k=TOP_K)

  chunks =[]

  for d, s in docs:
    chunks.append(d.page_content.strip())

  print("---before rerank---")
  for i, c in enumerate(chunks):
    print(f"--------chunk{i+1}-------")
    print(c)

  reranked = rerank_chunks(query, chunks)

  context_list = []
  print("---after reranked----")
  for i, (c,s) in enumerate(reranked):
    print(f"----chunk{i+1} | score{s:.2f}-----")
    print(c)

  for c,s in reranked:
    if s > RERANK_THRESHOLD:
      context_list.append(c)

  context_list = context_list[:2]
  context = "\n".join(context_list)
  return {"context": context}


def generate(state:MyState):
    prompt = GENERATE_PROMPT.format(
        query = state["query"],
        context = state["context"]
    )
    response = client.chat.completions.create(
        model = "openai/gpt-oss-120b",
        messages = [{"role":"user", "content":prompt}]
    )
    return {"answer": response.choices[0].message.content}