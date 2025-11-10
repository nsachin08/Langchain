
import os
import asyncio
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from lanchain.prebuilt import create_react_agent
from langchain.chat_models import init_chat_model
from langgraph_supervisor import create_supervisor


load_dotenv()

from langchain_core.messages import convert_to_messages


def format_msg(msg , indent=False):
    fmt_msg = msg.pretty_repr(html = True)
    if not indent:
        print(fmt_msg)
        return 
    
    indented = "\n".join("/t" + c for c in fmt_msg.split("\n"))
    print(indented)
