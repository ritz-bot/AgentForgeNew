""" from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults

from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

from app.config.settings import settings

def get_Response_from_ai_agents(llm_id, query , allow_search, system_prompt):

    llm=ChatGroq(model=llm_id)

    tools=[TavilySearchResults(max_results=2)] if allow_search else []

    agent = create_react_agent(
    llm=some_llm,  # Your LLM instance
    tools=some_tools,
    prompt="you are a medical ai agent specialised in cancer"  # Now uses 'prompt'
)

    

    state = {"messages": query}

    response = agent.invoke(state)

    messages = response.get("messages")

    ai_messages = [message.content for message in messages if isinstance(message,AIMessage)]

    return ai_messages[-1]

      """

from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults

from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage
from langchain_core.prompts import ChatPromptTemplate

from app.config.settings import settings

def get_Response_from_ai_agents(llm_id, query, allow_search, system_prompt):

    llm = ChatGroq(model=llm_id)

    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    # Create a prompt template with the system prompt
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", system_prompt)
    ])

    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=prompt_template
    )

    state = {"messages": query}

    response = agent.invoke(state)

    messages = response.get("messages")

    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]

    return ai_messages[-1]