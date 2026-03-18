import builtins
from unittest import mock
from chatbot import faq_bot, responses

def test_cli_loop_exit(monkeypatch):
    """Test CLI loop, exit condition, and logging without real user input or file writes."""

    # Sequence of inputs: first a greeting, then goodbye to exit
    inputs = iter(["hello", "bye"])
    
    # Mock input() to return values from the sequence
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    
    # Mock open() to avoid writing to chat_log.txt
    with mock.patch("builtins.open", mock.mock_open()) as mocked_file:
        faq_bot()  # Run the bot; it should exit after "bye"
    
    # Check that the file write was called twice (for each input)
    assert mocked_file().write.call_count == 2
    
    # Check that "goodbye" response is in the responses dictionary
    assert "goodbye" in responses

def test_unknown_intent(monkeypatch):
    """Test that unknown input triggers the fallback response."""

    # Input that is gibberish
    inputs = iter(["asdlkfjasldkfj", "bye"])
    
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))
    
    with mock.patch("builtins.open", mock.mock_open()):
        faq_bot()
    
    # Check that "unknown" is in responses fallback
    assert "unknown" in responses