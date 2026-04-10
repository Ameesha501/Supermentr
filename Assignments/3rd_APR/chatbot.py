# Simple Chatbot (Final Version)

def chatbot_response(user_input):
    text = user_input.lower()

    if "hello" in text or "hi" in text:
        return "Hello! How can I help you?"

    elif "name" in text:
        return "I am your NLP Mini Chatbot 🤖"

    elif "how are you" in text:
        return "I'm doing great! 😊"

    elif "what can you do" in text:
        return "I can chat with you and answer simple questions."

    elif "bye" in text:
        return "Goodbye! Have a nice day 👋"

    else:
        return "Sorry, I didn't understand that."


# main loop
while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Bye!")
        break

    response = chatbot_response(user_input)
    print("Chatbot:", response)