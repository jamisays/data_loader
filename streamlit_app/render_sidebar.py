import streamlit as st


def render_llm_sidebar():
    with st.sidebar:
        st.header("LLM Configuration")
        
        # Model selection with color coding
        model_options = ["OllamaChat", "Kluster.ai/DeepSeek-R1"]
        current_model = st.session_state.get("selected_model", "OllamaChat")

        new_model = st.selectbox(
            "Select LLM Model",
            model_options,
            index=model_options.index(current_model),
            format_func=lambda x: f"✅ {x}" if x == current_model else x,
            key="model_selector",
            help="Currently active model is highlighted with ✅"
        )
        
        # Update session state if model changes
        if new_model != current_model:
            st.session_state.selected_model = new_model 
            st.rerun()

        st.markdown("""
        <style>
            div[data-baseweb="select"] > div:first-child {
                background-color: %s;
            }
        </style>
        """ % ("#e6ffe6" if st.session_state.selected_model == "OllamaChat" else "#ffe6e6"),
        unsafe_allow_html=True)
        
        # Kluster.ai specific inputs
        if st.session_state.selected_model == "Kluster.ai/DeepSeek-R1":
            st.divider()
            api_key = st.text_input(
                "API Key",
                type="password",
                value=st.session_state.get("kluster_api_key", ""),
                key="kluster_api_input",
                help="Enter your Kluster.ai API key"
            )
            
            if st.button("🚀 Apply Configuration", use_container_width=True):
                if len(api_key) < 32:  # Basic validation
                    st.error("Please enter a valid API key")
                else:
                    st.session_state.kluster_api_key = api_key
                    st.success("Model configuration updated!")

        # Visual separator
        st.divider()
        st.markdown("ℹ️ Select your preferred LLM and configure credentials")