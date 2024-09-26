from datetime import datetime
def chatbot():
    print("Hello! I'm a simple chatbot. How can I help you today?")
    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ['hi', 'hello', 'hey']:
            print("Chatbot: Hello! How can I assist you?")
        elif user_input in ['how are you', 'how are you doing']:
            print("Chatbot: I'm just a bunch of code, but I'm here to help you!")
        elif user_input in ['what is your name', 'who are you']:
            print("Chatbot: I'm a simple chatbot created to help you with basic queries.")
        elif user_input in ['bye', 'goodbye', 'exit']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        elif 'weather' in user_input:
            print("Chatbot: I can't check the weather right now, but it's always a good idea to look outside!")
        elif 'time' in user_input:
            current_time = datetime.now().strftime('%H:%M')
            print(f"Chatbot: The current time is {current_time}.")
        elif 'favourite colour' in user_input:
            print("Chatbot: I'm a chatbot, so i dont have a favourite colour. But i like all colours!")
        elif 'age' in user_input:
            print("Chatbot: I'm a computer program. So i dont have a age!")
        elif 'what can u do' in user_input:
            print("Chatbot: I can provide information ,Time ,tell jokes and more .Just ask me!")
        elif 'joke' in user_input:
            print("Chatbot: Why don't scientists trust atoms? Because they make up everything!")
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you please rephrase?")

# Run the chatbot
chatbot()