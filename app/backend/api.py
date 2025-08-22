""" from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List
from app.core.ai_agent import get_Response_from_ai_agents
from app.config.settings import settings
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

import traceback
import logging

logging.basicConfig(level=logging.DEBUG)

logger = get_logger(__name__)

app = FastAPI(title="MULTI AI AGENT")

class RequestState(BaseModel):
    model_name:str
    system_prompt:str
    messages:List[str]
    allow_search: bool

@app.post("/chat")
def chat_endpoint(request:RequestState):
    logger.info(f"Received request for model : {request.model_name}")

    if request.model_name not in settings.ALLOWED_MODEL_NAMES:
        logger.warning("Invalid model name")
        raise HTTPException(status_code=400 , detail="Invalid model name")
    
    try:
        response = get_Response_from_ai_agents(
            request.model_name,
            request.messages,
            request.allow_search,
            request.system_prompt
        )

        logger.info(f"Sucesfully got response from AI Agent {request.model_name}")

        return {"response" : response}
    
    except Exception as e:
        logger.error("Some error ocuured during reponse generation")
        raise HTTPException(
            status_code=500 , 
            detail=str(CustomException("Failed to get AI response" , error_detail=e))
            )
    


 """

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from app.core.ai_agent import get_Response_from_ai_agents
from app.config.settings import settings
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

import traceback
import logging

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
    logger.debug(f"Allowed models: {settings.ALLOWED_MODEL_NAMES}")  # Added for debugging

    if request.model_name not in settings.ALLOWED_MODEL_NAMES:
        logger.warning(f"Invalid model name: {request.model_name}. Allowed: {settings.ALLOWED_MODEL_NAMES}")
        raise HTTPException(status_code=400, detail=f"Invalid model name: {request.model_name}. Allowed models: {settings.ALLOWED_MODEL_NAMES}")
    
    try:
        response = get_Response_from_ai_agents(
            request.model_name,
            request.messages,
            request.allow_search,
            request.system_prompt
        )

        logger.info(f"Successfully got response from AI Agent {request.model_name}")

        return {"response": response}
    
    except Exception as e:
        logger.error(f"Error during response generation: {str(e)}")
        logger.error(traceback.format_exc())  # Log full traceback
        raise HTTPException(
            status_code=500, 
            detail=str(CustomException("Failed to get AI response", error_detail=e))
        )
