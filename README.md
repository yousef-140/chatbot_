# 🤖 Yousef Reda Chatbot

This is a simple chatbot project built with:

- 🧠 FastAPI (for backend)
- 🌐 Streamlit (for frontend)
- 🔗 Local API calls (to simulate AI responses)

## 🚀 How to Run the Project

### 1. Clone the repository:

```bash
git clone https://github.com/yousef-140/chatbot_.git
cd chatbot_
```

### 2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
venv\Scripts\activate   # On Windows
# source venv/bin/activate   # On Linux/Mac
```

### 3. Install dependencies:

```bash
pip install -r requirements.txt
```

### 4. Run FastAPI backend:

```bash
uvicorn app:app --reload --port 8001
```

### 5. Run Streamlit frontend:

```bash
streamlit run your_frontend_file.py
```

> Replace `your_frontend_file.py` with the name of your Streamlit file.

---

## 📝 Features

- Simple user interface with Streamlit
- Sends user input to FastAPI backend
- Backend processes and returns simulated chatbot replies
- Maintains chat history during session

---

## 📁 Project Structure

```
├── app.py                 # FastAPI backend
├── streamlit_app.py       # Streamlit frontend (you can rename it if needed)
├── fastAPI.ipynb          # Notebook for experimentation
├── README.md              # This file
```

---

## 📌 Notes

- Make sure FastAPI is running before starting the Streamlit app.
- You can modify the backend to connect to real AI models or APIs.

---

## 🧑‍💻 Created By

**Yousef Reda Hassan**
