# imports
import spacy

# load the English NLP model
nlp = spacy.load("en_core_web_sm")

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
    else:
        return "unknown"
    
# function to get output
def faq_bot():
    print("Hi! I'm your assistabt. Ask me anything!")

    while True:
        user_input = input("You: ")
        intent = get_intent(user_input)

        if intent == "greeting":
            print("Bot: Hello! How can I assist you today?")
        elif intent == "hours":
            print("Bot: We're open from 9AM to 5PM, Mon to Fri")
        elif intent == "location":
            print("Bot: We're located at 222 Main Drive, City")
        elif intent == "contact":
            print("Bot: You can contact us at email@email.com")
        elif intent == "goodbye":
            print("Bot: Goodbye! Have a great day!")
            break
        else:
            print("Bot: Not sure how to respond to that...")

# run the bot
faq_bot()