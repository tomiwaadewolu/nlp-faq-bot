from chatbot import get_intent

def test_empty_input():
    # Test handling of empty string input
    result = get_intent("")
    assert result is not None  # Should not crash or return None


def test_gibberish_input():
    # Test random/unrecognizable text
    result = get_intent("asdlkfjasldkfj")
    assert isinstance(result, str)  # Should still return an intent label


def test_special_characters():
    # Test input with only symbols
    result = get_intent("@@@!!!")
    assert isinstance(result, str)  # Should handle without errors


def test_long_input():
    # Test very long input string
    text = "hello " * 50
    result = get_intent(text)
    assert isinstance(result, str)  # Should process long text safely


def test_mixed_intent():
    # Test input containing multiple intents
    result = get_intent("hello, where are you located?")
    assert result in ["greeting", "location"]  # Accept either valid intent