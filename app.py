import streamlit as st
import requests

st.title(" Yousef Reda ChatBot")

# Create chat history if not exists
if "chat_hist" not in st.session_state:
    st.session_state.chat_hist = []

# Input box
query = st.text_input(" Enter your query:")

messages = []
for sender, msg in st.session_state.chat_hist:
    role = "user" if sender == "You" else "assistant"
    messages.append({"role": role, "content": msg})
# Button
if st.button("Send") and query.strip():
    # Send query to FastAPI
    messages.append({"role": "user", "content": query})
    response = requests.post("http://localhost:8001/llm/", json={"messages": messages})

    if response.status_code == 200:
        answer = response.json()["answer"]
        # Add to history
        st.session_state.chat_hist.append(("You", query))
        st.session_state.chat_hist.append((" Bot", answer))
        

# Display chat history
if st.session_state.chat_hist:
    st.subheader(" Chat History")
    for sender, msg in st.session_state.chat_hist:
        st.markdown(f"{sender}: {msg}")

#"Clear Chat" button
if st.button(" Clear Chat"):
    st.session_state.chat_hist = []
    st.success("Chat history cleared.")
