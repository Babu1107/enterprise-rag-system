ROUTER_PROMPT ="""
  You have to classify the user query from one of the below:
  -policy: travel policy, leave policy, accomodation, reimbrusement
  -weather: climate, forecast, temperature
  -unsupported: anything else
  query:{query}
  RETURN ONLY in JSON.
  Example:
  {{"action":"policy"}}

  {{"action":"weather"}}

  {{"action":"unsupported"}}
  """

RERANK_PROMPT = """
  RANK the chunks based on query
  query:{query}
  chunks:{chunks}

  RETURN JSON list of score between (0-1)
  example [0.90, 0.83,0.54]
  """
GENERATE_PROMPT = """

    You will receive context from one of the below:
    -company policy document
    -weather report

    query:{query}
    context:{context}

    based on the context answer clearly
    RETURN ONLY JSON
    {{
        "response":"",
        "reason":""
    }}
    """
