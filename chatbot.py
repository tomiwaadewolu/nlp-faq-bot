# imports
import spacy
from datetime import datetime # for logging

# load the English NLP model
nlp = spacy.load("en_core_web_sm")

# define the possible responses in a dictionary
responses = {
    "greeting": "Hello! How can I assist you today?",
    "hours": "We're open from 9AM to 5PM, Mon to Fri",
    "location": "We're located at 222 Main Drive, City",
    "contact": "You can contact us at email@email.com",
    "goodbye": "Goodbye! Have a great day!",
    "services": "We offer consulting, support, and development services",
    "pricing": "Please contact us at email@email.com for detailed pricing information",
    "help": "You can ask me about our hours, location, services, or contact information",
    "unknown": "Not sure how to respond to that..."
}

# function to get intent
def get_intent(user_input):
    doc = nlp(user_input.lower()) # to lower case

    # extract lemmatized tokens for better matchings
    # lemmatization (turning “contacted”, “contacting” → “contact”)
    lemmas = [token.lemma_ for token in doc]

    # simple keyword-based intent detection
    if "hello" in lemmas or "hi" in lemmas:
        return "greeting"
    elif "hour" in lemmas or "open" in lemmas:
        return "hours"
    elif "location" in lemmas or "where" in lemmas or "address" in lemmas:
        return "location"
    elif "contact" in lemmas or "email" in lemmas or "phone" in lemmas:
        return "contact"
    elif "bye" in lemmas or "exit" in lemmas or "goodbye" in lemmas:
        return "goodbye"
    elif "service" in lemmas or "offer" in lemmas:
        return "services"
    elif "price" in lemmas or "cost" in lemmas:
        return "pricing"
    elif "help" in lemmas:
        return "help"
    else:
        return "unknown"
    
# function to get output
def faq_bot():
    print("Hi! I'm your assistant. Ask me anything!")

    while True:
        user_input = input("You: ")
        intent = get_intent(user_input)
        bot_response = responses[intent]

        # print response from dictionary
        print("Bot: ", bot_response)

        # log conversation to a file
        with open("chat_log.txt", "a", encoding="utf-8") as log_file:
            log_file.write(f"{datetime.now()} | User: {user_input} | Bot: {bot_response}\n")

        # exit condition
        if intent == "goodbye":
            break

# run the bot
if __name__ == "__main__":
    faq_bot()