from langchain_ollama import ChatOllama
import streamlit as st
from langchain_openai import ChatOpenAI


def get_llm():
    model = st.session_state.get("selected_model", "OllamaChat")

    if model == "OllamaChat":
        return ChatOllama(model="llama3.1:8b", streaming=True)
    elif model == "Kluster.ai/DeepSeek-R1":
        if not st.session_state.get("kluster_api_key"):
            raise ValueError("Kluster.ai API key is missing")
        
        return ChatOpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=st.session_state.kluster_api_key,
            model="google/gemini-2.0-flash-lite-preview-02-05:free"
        )
    else:
        raise ValueError(f"Unknown model: {model}")