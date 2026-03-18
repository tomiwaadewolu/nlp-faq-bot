from chatbot import preprocess

def test_lowercase():
    # Ensure text is converted to lowercase
    assert preprocess("HELLO") == "hello"

def test_lemmatization():
    # Ensure words are lemmatized (e.g., "contacting" → "contact")
    result = preprocess("contacting you")
    assert "contact" in result

def test_output_type():
    # Ensure the output of preprocessing is a string
    result = preprocess("hello")
    assert isinstance(result, str)