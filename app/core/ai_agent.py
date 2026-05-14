from typing import Iterable

from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage
from langgraph.errors import GraphRecursionError
from langgraph.prebuilt import create_react_agent

from app.config.settings import settings


def _stringify_content(content) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        text_parts = []
        for item in content:
            if isinstance(item, dict) and item.get("type") == "text":
                text_parts.append(item.get("text", ""))
            else:
                text_parts.append(str(item))
        return "".join(text_parts).strip()
    return str(content)


def _normalize_messages(query) -> list[BaseMessage]:
    if isinstance(query, str):
        query = [query]

    messages: list[BaseMessage] = []
    for item in query:
        if isinstance(item, BaseMessage):
            messages.append(item)
            continue

        text = str(item).strip()
        if text:
            messages.append(HumanMessage(content=text))

    if not messages:
        raise ValueError("User query cannot be empty.")

    return messages


def _resolve_system_prompt(system_prompt: str) -> str:
    prompt = system_prompt.strip()
    return prompt or settings.DEFAULT_SYSTEM_PROMPT


def _chat_without_tools(llm: ChatGroq, messages: Iterable[BaseMessage], system_prompt: str) -> str:
    response = llm.invoke([SystemMessage(content=system_prompt), *messages])
    return _stringify_content(response.content)


def get_Response_from_ai_agents(llm_id, query, allow_search, system_prompt):
    llm = ChatGroq(model=llm_id)
    normalized_messages = _normalize_messages(query)
    resolved_system_prompt = _resolve_system_prompt(system_prompt)

    if not allow_search:
        return _chat_without_tools(llm, normalized_messages, resolved_system_prompt)

    tools = [TavilySearchResults(max_results=2)]

    agent = create_react_agent(
        model=llm,
        tools=tools,
        prompt=f"{resolved_system_prompt}\n\nUse the web search tool only when it is necessary.",
    )

    try:
        response = agent.invoke(
            {"messages": normalized_messages},
            config={"recursion_limit": settings.AGENT_RECURSION_LIMIT},
        )
    except GraphRecursionError:
        fallback_response = _chat_without_tools(llm, normalized_messages, resolved_system_prompt)
        return (
            f"{fallback_response}\n\n"
            "[Note: Web search agent hit the tool-use limit, so this response was generated without search.]"
        )

    messages = response.get("messages", [])
    ai_messages = [
        _stringify_content(message.content)
        for message in messages
        if isinstance(message, AIMessage) and _stringify_content(message.content)
    ]

    if not ai_messages:
        raise ValueError("The selected model did not return a response.")

    return ai_messages[-1]
