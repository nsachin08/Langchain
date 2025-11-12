# Agents

agent combines LLMs with tools 

## Core Components

1. Model -> model is the reasoning agent

a. Static Model -> configured once and remain unchanged throught the execution
b. Dyanmic Model -> configured using middleware and based on required can be switched

2. Tools

tools gives agent the ability to take actions

a. Multiple tools can be called in sequence
b. Parallel tools calls 
c. Dynamic tool selection based on previous results
d. Tool retry logic and error handling
e. State Persistence across tools calls

Tool error Message

Tool use in ReAct Loop

3. System Prompt

system prompt  can be provided as a attribute while create_agent

agent = create_agent(
    model,
    tools,
    system_prompt="You are a helpful assistant. Be concise and accurate."
)

### When no system_prompt is provided, the agent will infer its task from the messages directly.

3.1 Dynamic System Prompt


