import streamlit as st
from langchain.callbacks.streamlit import StreamlitCallbackHandler

def init_chat_history():
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "assistant", "content": "How can I help you?"}]

def render_chat_messages():
    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

def handle_user_input(agent):
    user_query = st.chat_input(placeholder="Ask anything...")
    
    if user_query:
        st.session_state.messages.append({"role": "user", "content": user_query})
        st.chat_message("user").write(user_query)

        with st.chat_message("assistant"):
            st_callback = StreamlitCallbackHandler(st.container())
            response = agent.run(user_query, callbacks=[st_callback])
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.write(response)