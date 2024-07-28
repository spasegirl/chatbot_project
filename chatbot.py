from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


model_name = "microsoft/DialoGPT-medium"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def chatbot_response(user_input, chat_history_ids=None):
    # encod new user input
    new_user_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
    
    # appending the new user input tokens to the chat history
    if chat_history_ids is not None:
        bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1)
    else:
        bot_input_ids = new_user_input_ids

    #  response
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    # decoding the response
    response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    return response, chat_history_ids

## In case of running the chatbot in the terminal uncomment the following
""" if __name__ == "__main__":
    print("Im ready to talk to you <3.")
    chat_history_ids = None
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            print("Chatbot: Bye, take care. See you soon :)")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}") """
