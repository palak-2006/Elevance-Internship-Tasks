import streamlit as st
from sentiment import analyze_sentiment

st.set_page_config(
    page_title="Sentiment Analysis Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Sentiment Analysis Chatbot")
st.write("Enter a message and I'll detect its sentiment.")

user_input = st.text_area("Your Message")

if st.button("Analyze Sentiment"):

    if user_input.strip():

        sentiment, score = analyze_sentiment(user_input)

        st.subheader("Detected Sentiment")
        st.success(sentiment)

        st.subheader("Confidence Score")
        st.write(f"Compound Score: {score['compound']}")

        if "Positive" in sentiment:
            response = (
                "😊 I'm glad you're feeling positive! "
                "Thank you for your feedback."
            )

        elif "Negative" in sentiment:
            response = (
                "😔 I'm sorry you're having a bad experience. "
                "Please tell me more so I can help."
            )

        else:
            response = (
                "😐 Thank you for your message. "
                "How can I assist you further?"
            )

        st.subheader("Chatbot Response")
        st.info(response)

    else:
        st.warning("Please enter a message.")