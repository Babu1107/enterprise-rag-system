import time

import mlflow
import json
import mlflow

from graph_builder import app
from config import  (
  MODEL_NAME,
  EMBEDDING_MODEL,
  CHUNK_SIZE,
  CHUNK_OVERLAP,
  TOP_K,
  RERANK_THRESHOLD)

mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("Enterprise-RAG-System")

query = input("Ask: ")

start = time.time()

with mlflow.start_run():
  result = app.invoke({"query":query})

  end = time.time()

  latency = end - start

  #==================
  #MLFLOW PARAMETERS
  #===================
  mlflow.log_param("llm_model", MODEL_NAME)
  mlflow.log_param("embedding_model", EMBEDDING_MODEL)
  mlflow.log_param("chunk_size", CHUNK_SIZE)
  mlflow.log_param("chunk_overlap", CHUNK_OVERLAP)
  mlflow.log_param("top-k", TOP_K)
  mlflow.log_param("rerank_threshold", RERANK_THRESHOLD)
  mlflow.log_param("query", query)
  mlflow.log_param("router_decision", result.get("decision", ""))

  #==================
  #MLFLOW METRICS
  #===================
  mlflow.log_metric("latency", latency)

  #==================
  #MLFLOW ARTIFACTS
  #===================
  mlflow.log_text(
      result["context"],
      "retrieved_context.txt"
  )

  mlflow.log_text(
      result["answer"],
      "response.txt"
  )


  #========================
  #Store Parameters as JSON
  #========================

  params = {
      "llm_model": MODEL_NAME,
      "embedding_model": EMBEDDING_MODEL,
      "chunk_size": CHUNK_SIZE,
      "chunk_overlap": CHUNK_OVERLAP,
      "top_k":TOP_K,
      "rerank_threshold": RERANK_THRESHOLD,
      "query":query,
      "router_decision": result.get("decision","")
  }

  mlflow.log_text(
      json.dumps(params, indent =4),
      "parameters.json"
  )


  #========================
  #Store Metrics as JSON
  #========================

  metrics = {
      "latency": latency
  }

  mlflow.log_text(
      json.dumps(metrics, indent=4),
      "metrics.json"
  )
  print(result["answer"])
  #===================
  mlflow.log_metric("latency", latency)

  #==================
  #MLFLOW ARTIFACTS
  #===================
  mlflow.log_text(
      result["context"],
      "retrieved_context.txt"
  )

  mlflow.log_text(
      result["answer"],
      "response.txt"
  )


  #========================
  #Store Parameters as JSON
  #========================

  params = {
      "llm_model": MODEL_NAME,
      "embedding_model": EMBEDDING_MODEL,
      "chunk_size": CHUNK_SIZE,
      "chunk_overlap": CHUNK_OVERLAP,
      "top_k":TOP_K,
      "rerank_threshold": RERANK_THRESHOLD,
      "query":query,
      "router_decision": result.get("decision","")
  }

  mlflow.log_text(
      json.dumps(params, indent =4),
      "parameters.json"
  )


  #========================
  #Store Metrics as JSON
  #========================

  metrics = {
      "latency": latency
  }

  mlflow.log_text(
      json.dumps(metrics, indent=4),
      "metrics.json"
  )
  print(result["answer"])
