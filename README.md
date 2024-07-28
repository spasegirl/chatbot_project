# chatbot_project

# AI Chatbot Project

Welcome to my first AI Chatbot project! This project demonstrates how to create a simple chatbot using Python, Flask, and the DialoGPT model from Hugging Face. 

## Prerequisites

 Make sure you have the following installed:

   -  Python 3.7 or higher


## Installation

 Clone the repository:
```
    git clone https://github.com/spasegirl/chatbot_project
    cd chatbot_project
```

Install the required libraries:
```
pip install -r requirements.txt
```
## Usage
 Run the Flask application:
```
python app.py
```

Open your browser and go to http://127.0.0.1:5000/ to talk with the chatbot.


## How It Works
- The chatbot.py script loads the DialoGPT model and tokenizer from Hugging Face's model hub.
- When a user inputs a message, the model generates a response based on the conversation history.
- The app.py script then sets up a Flask web server, serving the chat interface and handling AJAX requests for generating chatbot responses.




Have fun! <3