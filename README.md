# FAQ Chatbot (spaCy NLP)

A simple command-line FAQ chatbot built with Python using natural language processing from spaCy.
The chatbot detects user intent using lemmatization and simple keyword matching to respond to common questions like greetings, business hours, location, and contact information.

## 📌 Features

* Intent detection using NLP

* Lemmatization for better keyword matching

* Simple rule-based responses

* Continuous chat loop

* Clean and beginner-friendly Python implementation

## 🧠 How It Works

The chatbot processes user input using spaCy's NLP pipeline. The input text is:

* Converted to lowercase

* Tokenized

* Lemmatized (words are reduced to their base form)

Example:

contacted → contact

contacting → contact

This allows the bot to recognize similar intents even when the wording changes.

The bot then checks the processed tokens against predefined keywords to determine the user's intent.

Example intents:

* Greeting

* Business hours

* Location

* Contact information

* Pricing

* Services

* Exit / Goodbye

## 🛠 Technologies Used

* Python

* spaCy NLP library

## 📂 Project Structure

```
ai-projects/
│
├── chatbot.py        # Main chatbot script
├── README.md         # Project documentation
├── requirements.txt  # Dependencies
└── venv/             # Virtual environment (not recommended to push to GitHub)
```

## ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/ai-projects.git
cd ai-projects
```

### 2️⃣ Create a virtual environment

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

### 3️⃣ Install dependencies

```
pip install spacy
```

Download the English language model:

```
python -m spacy download en_core_web_sm
```

## ▶️ Running the Chatbot

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

## 📈 Future Improvements

* Add more intents and responses

* Use machine learning for intent classification

* Add a web interface using Flask or FastAPI

* Store responses in a database

* Integrate with messaging platforms

## 🎓 Learning Goals

This project demonstrates:

* Basic Natural Language Processing

* Intent recognition

* Rule-based chatbot logic

* Python project structure

It is designed as a beginner NLP project for learning how conversational bots work.