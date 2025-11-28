from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

st.title("💬 Gemini Chatbot (LangChain)")
st.sidebar.header("Settings")

MODEL_OPTIONS = [
    "models/gemini-pro-latest",
    "models/gemini-2.5-pro",
    "models/gemini-2.5-flash",
]

selected_model = st.sidebar.selectbox("Choose Gemini model", MODEL_OPTIONS, index=0)



st.session_state.setdefault("selected_model", selected_model)
st.session_state["selected_model"] = selected_model
st.session_state.setdefault("user_key", user_key)
st.session_state["user_key"] = user_key




if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_prompt = st.chat_input("Ask Gemini...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    llm = ChatGoogleGenerativeAI(
        model=selected_model,  # pick a valid model ID
        temperature=0.0,
    )

    response = llm.invoke(user_prompt)
    assistant_response = response.content

    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})
    with st.chat_message("assistant"):

        st.markdown(assistant_response)
