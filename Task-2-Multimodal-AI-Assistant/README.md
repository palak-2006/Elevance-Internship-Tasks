# Task 2 - Multi-Modal AI Assistant

## Overview

This project is a Multi-Modal AI Assistant built using Python and Google's Gemini API. The assistant can understand both text and image inputs, analyze visual content, maintain conversation memory, and generate context-aware responses.

## Features

* Image understanding and analysis
* Text-based question answering
* Multi-turn conversation memory
* Context-aware responses
* Evidence-based reasoning
* Ambiguity handling
* Gemini AI integration

## Technologies Used

* Python
* Google Gemini API
* Pillow (PIL)
* Python Dotenv
* JSON Memory Storage

## Project Structure

Task-2-Multimodal-AI-Assistant/

├── assistant.py

├── requirements.txt

├── README.md

├── .gitignore

└── memory.json

## How to Run

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies:

pip install -r requirements.txt

4. Create a .env file and add:

GEMINI_API_KEY=your_api_key

5. Run:

python assistant.py

## Example Usage

* Upload an image
* Ask questions such as:

  * What objects are visible?
  * What colors are present?
  * Describe the scene.
  * Is there any text in the image?

The assistant analyzes the image and provides a detailed response using Gemini AI.
