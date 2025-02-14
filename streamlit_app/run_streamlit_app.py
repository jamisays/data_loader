import streamlit as st
from .agent_setup import create_agent
from .render_sidebar import render_llm_sidebar
from .ui import handle_user_input, init_chat_history, render_chat_messages


def run_streamlit_app():
    print("Loaded streamlit app")
    st.set_page_config(
        page_title="Job Description Analyzer",
        initial_sidebar_state="expanded"  # <-- Add this line
    )
    # Initialization
    if 'selected_model' not in st.session_state:
        st.session_state['selected_model'] = 'OllamaChat'
    
    # Render components
    render_llm_sidebar()
    
    # Initialize database and agent
    try:
        from db.connect_for_st import get_db_connection_2
        db_connection = get_db_connection_2()
        agent = create_agent(db_connection)
    except Exception as e:
        st.error(f"Failed to initialize agent: {str(e)}")
        st.stop()
    
    # Existing chat components
    init_chat_history()
    render_chat_messages()
    handle_user_input(agent)