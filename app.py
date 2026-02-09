"""Real Estate Assistant - Chainlit App. Run with: chainlit run app.py"""

import chainlit as cl
from agents import Runner, set_default_openai_key
from config import get_config
from agent_defs import property_agent
from utils.logging import get_logger

logger = get_logger(__name__)

def _ensure_config():
    cfg = get_config()
    set_default_openai_key(cfg["openai_api_key"])
    return cfg

@cl.on_chat_start
async def on_chat_start():
    try:
        _ensure_config()
        cl.user_session.set("chat_history", None)
        await cl.Message(content="**Real Estate Assistant** - Mortgage eligibility, property recommendations, multilingual support. Ask anything about buying property.", author="Real Estate").send()
    except ValueError as e:
        await cl.Message(content="Configuration Error: " + str(e), author="System").send()
        raise

@cl.on_message
async def on_message(message: cl.Message):
    user_content = message.content.strip()
    if not user_content:
        await cl.Message(content="Please describe your real estate need.", author="Real Estate").send()
        return
    try:
        _ensure_config()
        logger.info("Processing: %s", user_content[:80])
        result = await Runner.run(property_agent, user_content)
        await cl.Message(content=result.final_output, author="Real Estate").send()
        logger.info("Response sent")
    except Exception:
        logger.exception("Query failed")
        await cl.Message(content="Something went wrong. Please try again.", author="Real Estate").send()
