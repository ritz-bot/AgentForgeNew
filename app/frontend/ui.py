import requests
import streamlit as st

from app.common.logger import get_logger
from app.config.settings import settings

logger = get_logger(__name__)

st.set_page_config(page_title="Multi AI Agent", layout="centered")
st.title("Multi AI Agent using Groq and Tavily")

system_prompt = st.text_area("Define your AI Agent:", height=70)
selected_model = st.selectbox("Select your AI model:", settings.ALLOWED_MODEL_NAMES)
allow_web_search = st.checkbox("Allow web search")
user_query = st.text_area("Enter your query:", height=150)


def _extract_error_message(response: requests.Response) -> str:
    try:
        payload = response.json()
        return payload.get("detail", "Backend returned an unknown error.")
    except ValueError:
        return response.text or "Backend returned an unknown error."


if st.button("Ask Agent") and user_query.strip():
    payload = {
        "model_name": selected_model,
        "system_prompt": system_prompt,
        "messages": [user_query],
        "allow_search": allow_web_search,
    }

    try:
        logger.info("Sending request to backend")
        response = requests.post(
            settings.BACKEND_URL,
            json=payload,
            timeout=settings.BACKEND_TIMEOUT_SECONDS,
        )

        if response.status_code == 200:
            agent_response = response.json().get("response", "")
            logger.info("Successfully received response from backend")

            st.subheader("Agent Response")
            st.markdown(agent_response.replace("\n", "<br>"), unsafe_allow_html=True)
        else:
            error_message = _extract_error_message(response)
            logger.error(f"Backend error: {error_message}")
            st.error(error_message)

    except requests.RequestException as exc:
        logger.error(f"Error occurred while sending request to backend: {exc}")
        st.error(f"Failed to communicate with backend: {exc}")
