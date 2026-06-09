def get_response(query, history=None):

    query = query.lower()

    if history is None:
        history = []

    # Last 5 messages context
    context = " ".join(
        [
            item.get("english_query", "").lower()
            for item in history[-5:]
        ]
    )

    # Machine Learning

    if "machine learning" in query:

        return """
Machine Learning is a branch of Artificial Intelligence (AI) that enables computers to learn from data and improve performance without being explicitly programmed.

Applications:
• Recommendation Systems
• Image Recognition
• Chatbots
• Fraud Detection
• Healthcare Prediction
"""

    # Advantages

    elif (
        "advantage" in query
        or "advantages" in query
        or "benefit" in query
    ):

        if "machine learning" in context:

            return """
Advantages of Machine Learning:

1. Automation of repetitive tasks
2. Better predictions
3. Improved accuracy
4. Faster decision making
5. Pattern recognition
6. Personalized recommendations
"""

        return """
Advantages depend on the topic being discussed.
"""

    # Disadvantages

    elif (
        "disadvantage" in query
        or "limitations" in query
        or "drawback" in query
    ):

        if "machine learning" in context:

            return """
Disadvantages of Machine Learning:

1. Requires large datasets
2. Can be computationally expensive
3. Risk of biased predictions
4. Difficult to interpret some models
"""

        return """
Please specify which topic you are asking about.
"""

    # AI

    elif (
        "artificial intelligence" in query
        or query == "ai"
        or "what is ai" in query
    ):

        return """
Artificial Intelligence (AI) is the simulation of human intelligence in machines that can think, learn, reason and make decisions.
"""

    # Python

    elif "python" in query:

        return """
Python is a powerful programming language widely used in:

• Artificial Intelligence
• Machine Learning
• Data Science
• Web Development
• Automation
"""

    # Data Science

    elif "data science" in query:

        return """
Data Science is the process of extracting meaningful insights from data using:

• Statistics
• Machine Learning
• Data Visualization
• Programming
"""

    # Explain It

    elif (
        "explain" in query
        or "details" in query
    ):

        if "machine learning" in context:

            return """
Machine Learning works by training algorithms on data. The model learns patterns from historical data and then makes predictions on new unseen data.

Common Types:
• Supervised Learning
• Unsupervised Learning
• Reinforcement Learning
"""

        if "artificial intelligence" in context:

            return """
Artificial Intelligence focuses on creating systems that can mimic human intelligence such as learning, reasoning and problem solving.
"""

    # Follow-up

    elif (
        "what about it" in query
        or "tell me more" in query
        or "more" == query.strip()
    ):

        if "machine learning" in context:

            return """
Machine Learning is widely used in modern applications such as Netflix recommendations, self-driving cars, virtual assistants and healthcare diagnostics.
"""

    return """
Sorry, I do not know the answer yet.

Try asking about:
• Machine Learning
• Artificial Intelligence
• Python
• Data Science
"""