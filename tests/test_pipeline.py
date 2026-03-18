# Test complete pipeline: user input → intent prediction → response lookup

from chatbot import get_intent, responses

def test_full_pipeline_hours():
    # Predict intent for hours-related question
    intent = get_intent("what are your hours")
    # Retrieve the corresponding response
    response = responses[intent]
    # Check that the response mentions "open"
    assert "open" in response.lower()

def test_full_pipeline_contact():
    # Predict intent for contact-related question
    intent = get_intent("email please")
    # Retrieve the corresponding response
    response = responses[intent]
    # Check that the response mentions "contact"
    assert "contact" in response.lower()