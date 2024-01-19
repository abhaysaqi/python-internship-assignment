import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    ['kaise ho|kya haal (.*)',['Theek hu Aap btao','theek haal']],
    ['hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']],
    ['how are you', ["I'm doing well, thank you!", 'I m fine, how about you?']],
    ['what is your name', ["I'm a chatbot.", 'I go by many names, but you can call me Chatbot.']],
    ['bye|goodbye', ['Goodbye!', 'See you later!', 'Bye!']],
    ['(.*) your name', ['My name is Chatbot.']],
    ['(.*) help (.*)', ['I can assist you with various topics. What do you need help with?']],
    ['(.*)', ["I'm not sure how to respond to that.", 'Could you please rephrase that?']]
]

# Create a Chat instance
chatbot = Chat(pairs, reflections)

# Function to start the chat
def start_chat():
    print("Hello! I'm a simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("Chatbot: Goodbye! Have a great day.")
            break
        else:
            response = chatbot.respond(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    nltk.download('punkt')  # Download NLTK data for tokenization
    start_chat()
