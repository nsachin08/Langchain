from langchain.agents import create_agent

#Define tool
def get_price(item: str) -> str:
    """ Get price for an item """
    return f"It's always $500 for this {item}!"

#Create Agent
agent = create_agent(
    model= "claude-sonnet-4-5-20250929",
    tools = [get_price],
    system_prompt="You are helpful assistant",
)

# Run the Agent

agent.invoke(
    {"messages": [{"role": "user", "content":"what is the price for apple watch"}]}
)

