# 🏥 Medical Q&A Chatbot

## Overview

This project is a Medical Question Answering Chatbot developed using the MedQuAD dataset. The chatbot retrieves the most relevant medical answer for a user's query using Natural Language Processing (NLP) techniques and TF-IDF based similarity matching.

The application is built with Streamlit and provides a simple user interface for asking medical questions.

## Features

* Medical Question Answering
* Retrieval-based chatbot
* Uses MedQuAD medical dataset
* TF-IDF Vectorization
* Cosine Similarity Matching
* Basic Medical Entity Recognition
* Interactive Streamlit User Interface

## Technologies Used

* Python
* Streamlit
* Scikit-Learn
* XML Parsing
* TF-IDF Vectorizer
* Cosine Similarity

## Dataset

Dataset Used: MedQuAD (Medical Question Answering Dataset)

The dataset contains medical question-answer pairs collected from trusted health sources.

Dataset Structure:

* XML files
* Question-Answer pairs
* Medical topics such as diseases, symptoms, diagnosis, treatment, and prognosis

## Project Structure

Task-3-Medical-QA-Chatbot/

├── app.py

├── README.md

├── requirements.txt

└── dataset/

```
└── 1_CancerGov_QA/

    ├── 0000001_1.xml

    ├── 0000001_2.xml

    └── ...
```

## How It Works

1. Load medical question-answer pairs from XML files.
2. Extract questions and answers.
3. Convert questions into TF-IDF vectors.
4. Accept user question through Streamlit interface.
5. Calculate cosine similarity between user query and dataset questions.
6. Return the most relevant answer.
7. Detect basic medical entities such as symptoms, diseases, and treatments.

## Installation

Install required packages:

pip install -r requirements.txt

## Run the Application

streamlit run app.py

## Example Questions

* What is Adult Acute Lymphoblastic Leukemia?
* What are the symptoms of Adult Acute Lymphoblastic Leukemia?
* How to diagnose Adult Acute Lymphoblastic Leukemia?
* What are the treatments for Adult Acute Lymphoblastic Leukemia?

## Future Improvements

* Advanced Medical Entity Recognition
* Deep Learning Based Retrieval
* Semantic Search using Sentence Transformers
* Multi-dataset Support
* Chat History Feature

## Author

Kanha Agrawal

## Internship Task

Task 3: Medical Q&A Chatbot using MedQuAD Dataset
