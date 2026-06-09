from langdetect import detect
from deep_translator import GoogleTranslator


def detect_language(text):

    text_lower = text.lower()

    # Hindi Detection
    hindi_words = [
        "kya", "hai", "kaise",
        "kyu", "mujhe", "mera",
        "iske", "iska", "tum", "aap"
    ]

    for word in hindi_words:
        if word in text_lower:
            return "hi"

    # Spanish Detection
    if "¿" in text:
        return "es"

    spanish_words = [
        "qué",
        "hola",
        "gracias",
        "español",
        "cómo"
    ]

    for word in spanish_words:
        if word in text_lower:
            return "es"

    # German Detection
    german_words = [
        "was ist",
        "danke",
        "guten",
        "maschine",
        "lernen"
    ]

    for word in german_words:
        if word in text_lower:
            return "de"

    # Portuguese Detection
    portuguese_words = [
        "o que é",
        "obrigado",
        "aprendizado",
        "português",
        "inteligência"
    ]

    for word in portuguese_words:
        if word in text_lower:
            return "pt"

    # French Detection
    french_words = [
        "bonjour",
        "merci",
        "qu'est",
        "français"
    ]

    for word in french_words:
        if word in text_lower:
            return "fr"

    try:

        lang = detect(text)

        supported_languages = [
            "en",
            "hi",
            "es",
            "fr",
            "de",
            "pt"
        ]

        if lang in supported_languages:
            return lang

        return "en"

    except:
        return "en"


def translate_to_english(text):

    try:

        translated_text = GoogleTranslator(
            source="auto",
            target="en"
        ).translate(text)

        return translated_text

    except:

        return text


def translate_from_english(text, target_lang):

    try:

        translated_text = GoogleTranslator(
            source="en",
            target=target_lang
        ).translate(text)

        return translated_text

    except:

        return text