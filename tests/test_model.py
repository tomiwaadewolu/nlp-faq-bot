from chatbot import get_intent

def test_greeting_intent():
    # Check that a greeting input is classified correctly
    assert get_intent("hello") == "greeting"

def test_location_intent():
    # Check that a location-related question is classified correctly
    assert get_intent("where are you located") == "location"

def test_pricing_intent():
    # Check that a pricing-related question is classified correctly
    assert get_intent("what does it cost") == "pricing"