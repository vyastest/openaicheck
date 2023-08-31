import openai
import streamlit as st

# Add sidebar content
st.sidebar.title("ChatGPT-like clone")
st.sidebar.markdown("This app demonstrates a ChatGPT-like clone using Streamlit and the OpenAI API.")
st.sidebar.markdown("Enter your OpenAI API Key in the input field on the sidebar to get started.")

# Request API Key in the sidebar
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")
