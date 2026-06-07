import os
import xml.etree.ElementTree as ET
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Dataset Path
DATASET_FOLDER = "dataset/1_CancerGov_QA"

questions = []
answers = []

print("Loading Dataset...")

# Read XML Files
for file in os.listdir(DATASET_FOLDER):

    if file.endswith(".xml"):

        file_path = os.path.join(DATASET_FOLDER, file)

        try:
            tree = ET.parse(file_path)
            root = tree.getroot()

            qa_pairs = root.find("QAPairs")

            if qa_pairs:

                for qa in qa_pairs.findall("QAPair"):

                    question = qa.find("Question")
                    answer = qa.find("Answer")

                    if question is not None and answer is not None:

                        questions.append(question.text.strip())
                        answers.append(answer.text.strip())

        except Exception as e:
            print("Error reading:", file, e)

print(f"Dataset Loaded Successfully!")
print(f"Total Questions: {len(questions)}")

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words="english")
question_vectors = vectorizer.fit_transform(questions)

# Medical Entities
diseases = [
    "leukemia",
    "cancer",
    "diabetes",
    "asthma",
    "anemia"
]

symptoms = [
    "fever",
    "cough",
    "pain",
    "bleeding",
    "fatigue"
]

treatments = [
    "chemotherapy",
    "radiation",
    "surgery",
    "transplant"
]

print("\n===================================")
print(" Medical Q&A Chatbot ")
print(" Type 'exit' to quit")
print("===================================")

while True:

    user_question = input("\nAsk Medical Question: ")

    if user_question.lower() == "exit":
        print("Goodbye!")
        break

    # Entity Recognition
    detected_entities = []

    for disease in diseases:
        if disease.lower() in user_question.lower():
            detected_entities.append(f"Disease: {disease}")

    for symptom in symptoms:
        if symptom.lower() in user_question.lower():
            detected_entities.append(f"Symptom: {symptom}")

    for treatment in treatments:
        if treatment.lower() in user_question.lower():
            detected_entities.append(f"Treatment: {treatment}")

    if detected_entities:

        print("\nDetected Medical Entities:")

        for entity in detected_entities:
            print("-", entity)

    # Retrieval
    user_vector = vectorizer.transform([user_question])

    similarity_scores = cosine_similarity(
        user_vector,
        question_vectors
    )

    best_match_index = similarity_scores.argmax()

    best_score = similarity_scores[0][best_match_index]

    print("\nMost Relevant Question:")
    print(questions[best_match_index])

    print("\nSimilarity Score:")
    print(round(best_score, 2))

    print("\nAnswer:")
    print("=" * 50)

    answer = answers[best_match_index]

    if len(answer) > 2000:
        answer = answer[:2000] + "..."

    print(answer)

    print("\n" + "=" * 50)