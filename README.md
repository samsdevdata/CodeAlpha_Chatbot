# CodeAlpha_Chatbot

# 🤖 FAQ Chatbot

This is a simple FAQ chatbot built using Python and Streamlit.  
It allows users to ask questions and get matched answers from a list of 45 frequently asked questions.

## 🚀 How to Run

1. Install the required libraries:
```bash
pip install streamlit scikit-learn
```

2. Make sure both these files are in the same folder:
- `chatbot_app.py`
- `chatbot_faq_data.py`

3. Run the app:
```bash
streamlit run chatbot_app.py
```

4. The app will open in your browser at:
```
http://localhost:8501
```

## 📌 Features

- Matches similar questions even with spelling/capitalization differences
- Shows dropdown with top 3 closest matching questions
- Case-insensitive search
- Easy to use interface

## 🛠 Libraries Used

- `streamlit`
- `scikit-learn`
