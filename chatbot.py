

import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"what is your name ?",
        ["My name is Chatbot.",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"quit",
        ["Bye, take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
]

def chatbot_response(text):
    chat = Chat(pairs, reflections)
    return chat.respond(text)

if __name__ == "__main__":
    print("Chatbot ready to talk! Type 'quit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Bye, take care. See you soon :)")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
