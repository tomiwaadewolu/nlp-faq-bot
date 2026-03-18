# Shared setup for pytest (avoids repeating imports and setup in every test)

import sys
import os

# Add project root directory to Python path so tests can import project files
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from chatbot import get_intent, preprocess, responses
from app import app

@pytest.fixture
def client():
    # Create a test client for the Flask app (simulates API requests)
    app.config["TESTING"] = True  # Enable testing mode (better error handling)
    return app.test_client()

@pytest.fixture
def sample_inputs():
    # Provide reusable example inputs for different intents
    return {
        "greeting": "hello",
        "hours": "what time do you open",
        "location": "where are you located",
        "contact": "how can I contact you",
        "services": "what services do you offer",
        "pricing": "how much does it cost",
        "help": "help me",
        "goodbye": "bye"
    }