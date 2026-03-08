# FAQ Chatbot (spaCy NLP + Machine Learning)

A simple command-line FAQ chatbot built with Python using natural language processing from spaCy and a machine learning model for intent classification.
The chatbot detects user intent using lemmatization and TF-IDF + Logistic Regression, allowing it to respond to common questions like greetings, business hours, location, and contact information.

## Features

* Intent detection using spaCy NLP and machine learning

* Lemmatization for better keyword matching

* TF-IDF (Term Frequency - Inverse Document Frequency) and Logistic Regression for intent classification

* Simple dictionary-based responses

* Continuous chat loop

* Automatic conversation logging with timestamps

* Clean and beginner-friendly Python implementation

## How It Works

1. Preprocessing:

   The chatbot processes user input using spaCy:
   - Converts text to lowercase
   - Tokenizes the text
   - Lemmatizes each word (e.g., `contacted → contact`, `contacting → contact`)

2. Feature Extraction:

   The preprocessed text is converted into numerical features using TF-IDF. This ensures the machine learning model can understand word importance and phrase patterns.

3. Intent Prediction:

   A Logistic Regression classifier predicts the intent based on the TF-IDF vector.
   Optionally, if the model is unsure (low probability), it can return "unknown".

4. Response Selection:

   Each intent is mapped to a predefined response dictionary. The bot replies accordingly.

Example intents:

- Greeting
- Business hours
- Location
- Contact information
- Services
- Pricing
- Help
- Exit / Goodbye
- Unknown (fallback when intent is unclear)

## Technologies Used

* Python

* spaCy NLP library

* scikit-learn (TF-IDF and Logistic Regression)

## Project Structure

```
nlp-faq-bot/
│
├── chatbot.py        # Main chatbot script
├── train_model.py    # Model training script
├── training_data.py  # Training examples for intents
├── intent_model.pkl  # Saved trained model
├── vectorizer.pkl    # Saved TF-IDF vectorizer
├── README.md         # Project documentation
├── chat_log.txt      # Automatically generated conversation logs
├── requirements.txt  # Python dependencies
├── .gitignore        # Ignore venv, pycache, etc.
└── venv/             # Virtual environment (not recommended to push)
```

## Installation

### 1️. Clone the repository

```
git clone https://github.com/yourusername/nlp-faq-bot.git
cd nlp-faq-bot
```

### 2️. Create a virtual environment

```
python -m venv venv
```

Activate it:

**Windows**

```
venv\Scripts\activate
```

**Mac/Linux**

```
source venv/bin/activate
```

### 3️. Install dependencies

```
pip install -r requirements.txt
```

Download the English language model:

```
python -m spacy download en_core_web_sm
```

## Training the Model

Before running the chatbot, train the intent classification model:

```
python train_model.py
```

This will:
1. Preprocess the training sentences with spaCy
2. Convert them to TF-IDF vectors
3. Train a Logistic Regression classifier
4. Save the model and vectorizer for later use

## Running the Chatbot

Run the script:

```
python chatbot.py
```

Example interaction:

```
Hi! I'm your assistant. Ask me anything!

You: hello
Bot: Hello! How can I assist you today?

You: what are your hours
Bot: We're open from 9AM to 5PM, Mon to Fri

You: where are you located
Bot: We're located at 222 Main Drive, City

You: bye
Bot: Goodbye! Have a great day!
```

All conversations are automatically saved to `chat_log.txt` with timestamps.

## Future Improvements

* Add more diverse examples for each intent

* Implement confidence threshold and automatic fallback for unknown inputs

* Add a web interface using Flask or FastAPI

* Store responses in a database

* Integrate with messaging platforms

## Learning Goals

This project demonstrates:

* Natural Language Processing with spaCy

* Intent recognition using TF-IDF and Logistic Regression

* Rule-based response mapping

* Python project structure and modular code

* Conversation logging for real-world applications

It is designed as a beginner NLP project to understand how conversational bots work.
