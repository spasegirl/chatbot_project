from flask import Flask, render_template, request, jsonify
from chatbot import chatbot_response

app = Flask(__name__)

# Storing chat history in session
chat_history_ids = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    session_id = request.remote_addr  # user's IP address as session ID
    if session_id not in chat_history_ids:
        chat_history_ids[session_id] = None
    response, chat_history_ids[session_id] = chatbot_response(user_text, chat_history_ids[session_id])
    return jsonify(response=response)

if __name__ == "__main__":
    app.run(debug=True)
