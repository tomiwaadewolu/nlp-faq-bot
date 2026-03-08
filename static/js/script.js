const chatBody = document.getElementById("chat-body");
const userInput = document.getElementById("user-input");

// Send message when pressing Enter
userInput.addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

// Function to append messages
function appendMessage(message, sender="bot") {
    const msgDiv = document.createElement("div");
    msgDiv.classList.add("chat-message");
    msgDiv.classList.add(sender === "bot" ? "bot-msg" : "user-msg");

    const bubble = document.createElement("div");
    bubble.classList.add("msg-bubble");
    bubble.innerText = message;

    msgDiv.appendChild(bubble);
    chatBody.appendChild(msgDiv);

    // Scroll to bottom
    chatBody.scrollTop = chatBody.scrollHeight;
}

// Function to send messages
function sendMessage() {
    const message = userInput.value.trim();
    if (message === "") return;

    appendMessage(message, "user");
    userInput.value = "";

    // Send POST request to Flask backend
    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({message: message})
    })
    .then(response => response.json())
    .then(data => {
        appendMessage(data.response, "bot");
    })
    .catch(error => {
        appendMessage("Sorry, there was an error. Try again.", "bot");
        console.error("Error:", error);
    });
}