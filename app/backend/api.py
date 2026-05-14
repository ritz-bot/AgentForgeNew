import logging
import traceback
from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.common.logger import get_logger
from app.config.settings import settings
from app.core.ai_agent import get_Response_from_ai_agents

logging.basicConfig(level=logging.DEBUG)

logger = get_logger(__name__)

app = FastAPI(title="MULTI AI AGENT")


class RequestState(BaseModel):
    model_name: str
    system_prompt: str
    messages: List[str]
    allow_search: bool


@app.post("/chat")
def chat_endpoint(request: RequestState):
    logger.info(f"Received request for model: {request.model_name}")

    if request.model_name not in settings.ALLOWED_MODEL_NAMES:
        logger.warning(f"Invalid model name: {request.model_name}")
        raise HTTPException(status_code=400, detail=f"Invalid model name: {request.model_name}")

    try:
        response = get_Response_from_ai_agents(
            request.model_name,
            request.messages,
            request.allow_search,
            request.system_prompt,
        )

        logger.info(f"Successfully got response from AI Agent {request.model_name}")
        return {"response": response}

    except ValueError as exc:
        logger.error(f"Invalid request: {exc}")
        raise HTTPException(status_code=400, detail=str(exc))

    except Exception as exc:
        logger.error(f"Error during response generation: {exc}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(exc))
