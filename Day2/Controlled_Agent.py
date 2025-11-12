from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    model = "gpt-5",
    temparature = 0.1,
    max_tokens = 1000,
    timeout = 30
)

agent = create_agent(model, tools = tools)