import streamlit as st
import pandas as pd
import plotly.express as px
import random

from sentiment import analyze_sentiment

st.set_page_config(
    page_title="AI Sentiment Chatbot",
    page_icon="🤖",
    layout="wide"
)

# Chat History
if "history" not in st.session_state:
    st.session_state.history = []

st.title("🤖 AI Sentiment Analysis Chatbot")

st.write(
    "This chatbot detects Positive, Negative, and Neutral emotions "
    "and responds accordingly."
)

user_input = st.text_area(
    "Enter your message:",
    height=120
)

if st.button("Analyze Sentiment"):

    if user_input.strip():

        sentiment, score = analyze_sentiment(user_input)

        confidence = abs(score["compound"]) * 100

        st.subheader("Detected Sentiment")
        st.success(sentiment)

        st.metric(
            label="Confidence",
            value=f"{confidence:.1f}%"
        )

        # Response Logic
        positive_responses = [
            "😊 Glad to hear that!",
            "🎉 Thanks for your positive feedback!",
            "😄 That's wonderful!"
        ]

        negative_responses = [
            "😔 Sorry to hear that.",
            "🙏 I understand your concern.",
            "💙 Let me help resolve this issue."
        ]

        neutral_responses = [
            "😐 Thank you for your message.",
            "🤖 How can I assist you further?",
            "📌 Please provide more details."
        ]

        if "Positive" in sentiment:
            response = random.choice(
                positive_responses
            )

        elif "Negative" in sentiment:
            response = random.choice(
                negative_responses
            )

        else:
            response = random.choice(
                neutral_responses
            )

        st.subheader("Chatbot Response")
        st.info(response)

        # Pie Chart
        chart_data = pd.DataFrame(
            {
                "Sentiment": [
                    "Positive",
                    "Neutral",
                    "Negative"
                ],
                "Score": [
                    score["pos"],
                    score["neu"],
                    score["neg"]
                ]
            }
        )

        fig = px.pie(
            chart_data,
            names="Sentiment",
            values="Score",
            title="Sentiment Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # Save History
        st.session_state.history.append(
            {
                "User Message": user_input,
                "Sentiment": sentiment,
                "Confidence": round(
                    confidence,
                    2
                ),
                "Response": response
            }
        )

# Sidebar Dashboard
st.sidebar.title("📊 Dashboard")

total = len(st.session_state.history)

positive = len([
    x for x in st.session_state.history
    if "Positive" in x["Sentiment"]
])

negative = len([
    x for x in st.session_state.history
    if "Negative" in x["Sentiment"]
])

neutral = len([
    x for x in st.session_state.history
    if "Neutral" in x["Sentiment"]
])

st.sidebar.metric(
    "Total Messages",
    total
)

st.sidebar.metric(
    "Positive",
    positive
)

st.sidebar.metric(
    "Negative",
    negative
)

st.sidebar.metric(
    "Neutral",
    neutral
)

# Chat History
st.subheader("💬 Chat History")

if st.session_state.history:

    for chat in reversed(
        st.session_state.history
    ):

        st.write(
            f"👤 {chat['User Message']}"
        )

        st.write(
            f"📊 {chat['Sentiment']}"
        )

        st.write(
            f"🤖 {chat['Response']}"
        )

        st.write("---")

    df = pd.DataFrame(
        st.session_state.history
    )

    st.download_button(
        label="📥 Download Chat Report",
        data=df.to_csv(
            index=False
        ),
        file_name="chat_report.csv",
        mime="text/csv"
    )

else:
    st.info(
        "No conversation yet."
    )