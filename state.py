from typing import TypedDict

class MyState(TypedDict):
  query:str
  context:str
  answer:str
  decision:str