print("Hello! I am your friendly chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").strip().lower()

    if user_input == "hello":
        print("Chatbot: Hello! How can I help you today?")
    
    elif user_input == "how are you":
        print("Chatbot: I'm doing great! How about you?")
    
    elif user_input == "your name":
        print("Chatbot: I am ChatBot 1.0.")
    
    elif user_input == "weather":
        print("Chatbot: I cannot fetch live weather yet, but it's always sunny in the virtual world! 🌞")
    
    elif user_input == "features":
        print("Chatbot: I can greet you, tell my name, respond to weather, features, trending, and say goodbye!")
    
    elif user_input == "trending":
        print("Chatbot: Trending topics today include AI, technology, and space exploration!")
    
    elif user_input == "bye":
        print("Chatbot: Goodbye! Have a great day.")
        break
    
    else:
        print("Chatbot: Sorry, I cannot understand.")
