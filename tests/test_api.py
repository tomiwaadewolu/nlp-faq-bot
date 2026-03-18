def test_chat_route_success(client):
    # Send POST request to /chat with a sample message
    response = client.post("/chat", json={"message": "hello"})
    
    # Check request was successful (HTTP 200 OK)
    assert response.status_code == 200
    
    # Ensure response contains expected JSON key
    assert "response" in response.json


def test_chat_response_content(client):
    # Send POST request with greeting message
    response = client.post("/chat", json={"message": "hello"})
    
    # Check that bot reply contains "hello" (case-insensitive)
    assert "hello" in response.json["response"].lower()