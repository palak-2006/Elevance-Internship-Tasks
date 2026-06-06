import os
import json
from PIL import Image
from dotenv import load_dotenv
import google.generativeai as genai

# Load API Key
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

MEMORY_FILE = "memory.json"


# Load Memory
def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return []


# Save Memory
def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=4)


print("====================================")
print(" Multi-Modal AI Assistant")
print("====================================")

memory = load_memory()

while True:

    image_path = input(
        "\nEnter image path (or type 'skip'): "
    )

    question = input("Ask your question: ")

    if question.lower() == "exit":
        break

    context = ""

    for item in memory[-5:]:
        context += (
            f"User: {item['question']}\n"
            f"Assistant: {item['answer']}\n"
        )

    prompt = f"""
You are a Multi-Modal AI Assistant.

Rules:
1. Analyze image carefully.
2. Use evidence from image.
3. Explain reasoning.
4. If image is unclear, say so.
5. Use previous conversation context.

Conversation History:
{context}

Current Question:
{question}
"""

    try:

        if image_path.lower() != "skip":

            image = Image.open(image_path)

            response = model.generate_content(
                [prompt, image]
            )

        else:

            response = model.generate_content(
                prompt
            )

        answer = response.text

        print("\n====================")
        print("ANSWER")
        print("====================\n")
        print(answer)

        memory.append({
            "question": question,
            "answer": answer
        })

        save_memory(memory)

    except Exception as e:
        print("\nError:", e)