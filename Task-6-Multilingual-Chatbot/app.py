import streamlit as st

from translator import (
    detect_language,
    translate_to_english,
    translate_from_english
)

from chatbot import get_response


st.set_page_config(
    page_title="Multilingual AI Chatbot",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Multilingual AI Chatbot")

st.markdown("""
### Features

✅ Automatic Language Detection

✅ Manual Language Switching

✅ English, Hindi, Spanish, German, French, Portuguese

✅ Context Retention

✅ Conversation History

✅ Mixed Language Support
""")


# Session State

if "history" not in st.session_state:
    st.session_state.history = []


language_names = {
    "en": "English",
    "hi": "Hindi",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "pt": "Portuguese"
}

lang_map = {
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Portuguese": "pt"
}


# Language Selection

selected_language = st.selectbox(
    "Choose Language",
    [
        "Auto Detect",
        "English",
        "Hindi",
        "Spanish",
        "French",
        "German",
        "Portuguese"
    ]
)


# Input

user_input = st.text_input(
    "Ask a question:"
)


col1, col2 = st.columns(2)

with col1:
    send_button = st.button("Send")

with col2:
    clear_button = st.button("Clear Chat")


# Clear Chat

if clear_button:
    st.session_state.history = []
    st.rerun()


# Send

if send_button:

    if user_input.strip():

        # Detect Language

        if selected_language == "Auto Detect":

            detected_lang = detect_language(
                user_input
            )

        else:

            detected_lang = lang_map[
                selected_language
            ]

        # Convert to English

        english_query = translate_to_english(
            user_input
        )

        # Generate Answer

        response_en = get_response(
            english_query,
            st.session_state.history
        )

        # Translate Back

        final_response = translate_from_english(
            response_en,
            detected_lang
        )

        # Display

        st.success(
            f"Detected Language: {language_names.get(detected_lang, detected_lang)}"
        )

        st.info(final_response)

        # Save History

        st.session_state.history.append(
            {
                "user": user_input,
                "english_query": english_query,
                "bot": final_response,
                "lang": detected_lang
            }
        )


# History

st.subheader("📜 Conversation History")

if len(st.session_state.history) == 0:

    st.info("No conversation yet.")

else:

    for i, chat in enumerate(
        st.session_state.history
    ):

        st.markdown(
            f"### Chat {i+1}"
        )

        st.write(
            f"👤 User ({language_names.get(chat['lang'], chat['lang'])})"
        )

        st.write(
            chat["user"]
        )

        st.write(
            "🤖 Bot"
        )

        st.write(
            chat["bot"]
        )

        st.markdown("---")


# Debug Section

with st.expander(
    "Debug Information"
):

    if st.session_state.history:

        last_chat = st.session_state.history[-1]

        st.write(
            "Detected Language:",
            language_names.get(
                last_chat["lang"],
                last_chat["lang"]
            )
        )

        st.write(
            "Translated Query:",
            last_chat["english_query"]
        )

        st.write(
            "Total Chats:",
            len(st.session_state.history)
        )