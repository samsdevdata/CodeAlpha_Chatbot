import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from chatbot_faq_data import faq_data  # make sure this file is in the same folder

st.title("🤖 FAQ Chatbot")

# Get the list of FAQ questions
questions = list(faq_data.keys())

# User input
user_input = st.text_input("Ask a question about the internship:")

# Only proceed if something is typed
if user_input:
    # Prepare lowercase data for matching
    all_questions = [q.lower() for q in questions]
    all_data = [user_input.lower()] + all_questions

    # Vectorize
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(all_data)

    # Calculate cosine similarity
    similarity = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

    # Find top 3 most similar questions
    top_indices = similarity.argsort()[-3:][::-1]
    suggested_questions = [questions[i] for i in top_indices if similarity[i] > 0.1]

    if suggested_questions:
        selected_question = st.selectbox("Did you mean:", suggested_questions)
        st.write("### Answer:")
        st.write(faq_data[selected_question])
    else:
        st.warning("Sorry, I couldn't find a matching question.")
