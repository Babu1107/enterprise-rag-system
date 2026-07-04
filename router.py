import json
from state import MyState
from config import client, MODEL_NAME
from prompts import ROUTER_PROMPT



def think(state:MyState):
  prompt = ROUTER_PROMPT.format(
      query = state["query"]
  )

  response = client.chat.completions.create(
      model = "openai/gpt-oss-120b",
      messages = [{"role":"user", "content":prompt}]
  )

  return {"decision": response.choices[0].message.content}

def route(state:MyState):
  return json.loads(state["decision"])["action"]