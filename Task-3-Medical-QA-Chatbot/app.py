import streamlit as st
import xml.etree.ElementTree as ET
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -------------------------------
# Load XML Dataset
# -------------------------------
@st.cache_data
def load_dataset():
    questions = []
    answers = []

    dataset_folder = "dataset/1_CancerGov_QA"

    for filename in os.listdir(dataset_folder):
        if filename.endswith(".xml"):
            filepath = os.path.join(dataset_folder, filename)

            try:
                tree = ET.parse(filepath)
                root = tree.getroot()

                for qa in root.findall(".//QAPair"):
                    question = qa.find("Question")
                    answer = qa.find("Answer")

                    if question is not None and answer is not None:
                        q_text = question.text.strip() if question.text else ""
                        a_text = answer.text.strip() if answer.text else ""

                        if q_text and a_text:
                            questions.append(q_text)
                            answers.append(a_text)

            except Exception:
                pass

    return questions, answers


questions, answers = load_dataset()

# -------------------------------
# TF-IDF Model
# -------------------------------
vectorizer = TfidfVectorizer(stop_words="english")
question_vectors = vectorizer.fit_transform(questions)

# -------------------------------
# Answer Retrieval
# -------------------------------
def get_answer(user_question):
    user_vector = vectorizer.transform([user_question])

    similarities = cosine_similarity(user_vector, question_vectors)

    best_index = similarities.argmax()
    best_score = similarities[0][best_index]

    if best_score < 0.10:
        return "Sorry, I could not find a relevant answer."

    return answers[best_index]


# -------------------------------
# Medical Entity Recognition
# -------------------------------
def detect_entities(text):
    symptoms = [
        "fever",
        "cough",
        "pain",
        "headache",
        "fatigue",
        "bleeding",
        "weakness"
    ]

    diseases = [
        "cancer",
        "leukemia",
        "diabetes",
        "asthma"
    ]

    treatments = [
        "chemotherapy",
        "radiation",
        "surgery",
        "therapy"
    ]

    found = []

    for word in symptoms:
        if word.lower() in text.lower():
            found.append(f"Symptom: {word}")

    for word in diseases:
        if word.lower() in text.lower():
            found.append(f"Disease: {word}")

    for word in treatments:
        if word.lower() in text.lower():
            found.append(f"Treatment: {word}")

    return found


# -------------------------------
# Streamlit UI
# -------------------------------

st.set_page_config(
    page_title="Medical Q&A Chatbot",
    page_icon="🏥",
    layout="wide"
)

st.markdown(
    """
    <h1 style='text-align:center; color:#2E86C1;'>
    🏥 Medical Q&A Chatbot
    </h1>
    <h4 style='text-align:center;'>
    Ask medical questions using the MedQuAD Dataset
    </h4>
    <hr>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns([3, 1])

with col2:
    st.info(f"📚 Questions Loaded: {len(questions)}")

with col1:
    user_question = st.text_input(
        "🔍 Enter your medical question:",
        placeholder="Example: What are the symptoms of leukemia?"
    )

if st.button("Get Answer", use_container_width=True):

    if user_question.strip():

        answer = get_answer(user_question)

        st.markdown("## 📖 Answer")
        st.success(answer)

        entities = detect_entities(user_question)

        if entities:
            st.markdown("## 🧬 Detected Medical Entities")

            for entity in entities:
                st.write("✅", entity)

    else:
        st.warning("⚠ Please enter a question.")

st.markdown("---")

with st.expander("💡 Example Questions"):
    st.write("• What is Adult Acute Lymphoblastic Leukemia?")
    st.write("• What are the symptoms of Adult Acute Lymphoblastic Leukemia?")
    st.write("• How to diagnose Adult Acute Lymphoblastic Leukemia?")
    st.write("• What are the treatments for Adult Acute Lymphoblastic Leukemia?")

st.markdown(
    """
    <div style='text-align:center; color:gray'>
    Developed using MedQuAD Dataset | Streamlit | Scikit-Learn
    </div>
    """,
    unsafe_allow_html=True
)