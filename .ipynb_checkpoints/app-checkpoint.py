import streamlit as st
import requests

st.title("Yousef Reda ChatBot 💬")

# Create chat history if not exists
if "chat_hist" not in st.session_state:
    st.session_state.chat_hist = []

# Input box
query = st.text_input("Enter your query:")

# When Send button is pressed
if st.button("Send") and query.strip():
    # Send request to FastAPI
    response = requests.post("http://localhost:8001/llm/", json={"query": query})

    # Append question and answer to history
    answer = response.json()["answer"]
    st.session_state.chat_hist.append((" You", query))
    st.session_state.chat_hist.append((" Bot", answer))

# Display chat history
if st.session_state.chat_hist:
    st.subheader("Chat History")
    for sender, msg in st.session_state.chat_hist:
        st.markdown(f"**{sender}:** {msg}")
