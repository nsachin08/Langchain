from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_model_call , ModelRequest , ModelResponse

basic_model = ChatOpenAI(model="gpt-4o-mini")
advanced_model = ChatOpenAI(model="gpt-4o")


@wrap_model_call
def dynamic_model_selection(request: ModelRequest, handler) -> ModelResponse:
    """Choose model based on conversation complexity."""
    msg_count = len(request.state["message"])

    if msg_count > 10:
        model = advanced_model
    else :
        model = basic_model
    
    request.model = model
    return handler(request)

agent = create_agent(
    model = basic_model,
    tools = tools,
    middleware = [dynamic_model_selection]

)
