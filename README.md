# FAQ Chatbot (spaCy NLP + Machine Learning + Web Interface)

A simple FAQ chatbot built with Python using spaCy NLP and a machine learning model for intent classification.
The chatbot detects user intent using lemmatization and TF-IDF + Logistic Regression, allowing it to respond to common questions like greetings, business hours, location, and contact information.
It also includes a web interface built with Flask.

## Features

* Intent detection using spaCy NLP and machine learning

* Lemmatization for better keyword matching

* TF-IDF (Term Frequency - Inverse Document Frequency) and Logistic Regression for intent classification

* Simple dictionary-based responses

* Continuous chat loop in CLI

* Web-based chat interface with Flask

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
   If the model is unsure, it can return "unknown".

4. Response Selection:

   Each intent is mapped to a predefined response dictionary. The bot replies accordingly.

5. Web Interface:

   Users can interact via a browser. Messages are sent to the Flask backend, which uses the trained ML model to predict intent and return responses in real-time.

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

* Flask (web interface)

* HTML/CSS/JavaScript (frontend)

## Project Structure

```
nlp-faq-bot/
│
├── chatbot.py        # Main chatbot script (CLI)
├── train_model.py    # Model training script
├── training_data.py  # Training examples for intents
├── intent_model.pkl  # Saved trained model
├── vectorizer.pkl    # Saved TF-IDF vectorizer
├── app.py            # Flask web interface
├── templates/
│   └── index.html    # HTML page for web interface
├── static/
│   ├── css/
│   │   └── style.css # Styling for web interface
│   └── js/
│       └── script.js # JavaScript for frontend interactions
├── README.md         # Project documentation
├── chat_log.txt      # Automatically generated conversation logs
├── requirements.txt  # Python dependencies
├── .gitignore        # Ignore venv, pycache, etc.
└── venv/             # Virtual environment (not recommended to push)
```

## Installation

### 1️. Clone the repository

```
git clone https://github.com/tomiwaadewolu/nlp-faq-bot.git
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

### Command-Line Interface

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

### Web Interface (Flask)

```
python app.py
```

Open a browser and go to: `http://127.0.0.1:5000/`
- Type messages in the input box
- Press Enter or click Send
- The bot responds in real-time using the ML intent model

All conversations are automatically saved to `chat_log.txt` with timestamps.

## Future Improvements

* Add more diverse examples for each intent

* Implement confidence threshold and automatic fallback for unknown inputs

* Enhance web interface (styling, message history, user avatars)

* Store responses in a database

* Integrate with messaging platforms

## Learning Goals

This project demonstrates:

* Natural Language Processing with spaCy

* Intent recognition using TF-IDF and Logistic Regression

* Rule-based response mapping

* Flask-based web interface integration

* Python project structure and modular code

* Conversation logging for real-world applications

It is designed as a beginner NLP project to understand how conversational bots work.
