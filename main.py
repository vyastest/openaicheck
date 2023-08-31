import openai
import streamlit as st

st.title("Streamlit Chat Interface")

api_key = st.text_input("Enter your OpenAI API Key", type="password")
openai.api_key = api_key
