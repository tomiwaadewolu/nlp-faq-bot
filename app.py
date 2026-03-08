# Flask Web Interface

# imports
from flask import Flask, request, jsonify, render_template
from chatbot import get_intent, responses

# create a Flask application instance
app = Flask(__name__)

# home page route
@app.route("/")
def home():
    # render the index.html file
    return render_template("index.html")

# chat messages route
# POST requests with user input
@app.route("/chat", methods=["POST"])
def chat():
    # extract the user's message from the JSON payload
    user_message = request.json["message"]

    # use the chatbot's ML function to predict the intent of the user message
    intent = get_intent(user_message)

    # look up the response corresponding to the predicted intent
    # if intent is not recognized, use the "unknown" fallback response
    bot_response = responses.get(intent, responses["unknown"])

    # return the bot's response as a JSON object
    # the front-end JavaScript will read this response and display it
    return jsonify({"response": bot_response})

# start the Flask development server
# debug=True enables auto-reload and provides detailed error messages
if __name__ == "__main__":
    app.run(debug=True)