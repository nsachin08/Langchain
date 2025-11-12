from langchain.agents import create_agent

agent = create_agent(
    "gpt-5",
    tools = tools
)
