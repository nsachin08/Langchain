from langchain.tools import tools
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_tool_call
from langchain_core.messages import ToolMessage


@tool
def search(query: str ) -> str:
    """ Search for information. """
    return f"Results for: {query}"

@tool
def get_weather(location: str) -> str:
    """ Get weather information for a location """
    return f"Weather in {location}: Sunny , 72 F "

agent = create_agent(model, tools = [search,get_weather])

# Tools error handling
# Wrap Tool call

@wrap_tool_call
def handle_tool_erros(request, handler):
    """ Handle tool execution errors with custom messages. """
    try: 
        return handler(request)
    except Exception as e:
        return ToolMessage(
            content = f"Tool error: Please check your input and try again .({str(e)})"
            tool_call_id=request.tool_call["id"]
        )    
    
agent = create_agent(
    tools=[search, get_weather],
    middleware=[handle_tool_errors]
)    



