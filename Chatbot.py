import nltk
nltk.download("punkt")
nltk.download("wordnet")

import nltk
from nltk.stem import WordNetLemmatizer
import random

# Lemmatizer to process user input
lemmatizer = WordNetLemmatizer()

# Sample responses for different topics
responses = {
    "greeting": ["Hello!", "Hi there!", "Greetings!", "How can I help you today?"],
    "goodbye": ["Goodbye!", "Have a great day!", "See you later!", "Take care!"],
    "name": ["I'm Chatbot. What's your name?", "You can call me Chatbot!", "I'm a friendly bot created to assist you!"],
    "help": ["I can chat with you, answer basic questions, and keep you company!", "Feel free to ask me anything!"],
    "default": ["I'm not sure I understand. Can you rephrase?", "I'm here to chat. Let's talk!"]
}

# Keywords to identify intents
keywords = {
    "greeting": ["hi", "hello", "hey", "greetings"],
    "goodbye": ["bye", "goodbye", "see you", "take care"],
    "name": ["name", "who are you"],
    "help": ["help", "assist", "support"]
}

# Function to find the intent of the user's input
def identify_intent(user_input):
    tokens = nltk.word_tokenize(user_input.lower())
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]
    
    for intent, words in keywords.items():
        if any(word in lemmatized_tokens for word in words):
            return intent
    return "default"

# Main chatbot response function
def chatbot_response(user_input):
    intent = identify_intent(user_input)
    return random.choice(responses[intent])

# Chat function to start the conversation
def chat():
    print("Chatbot: Hello! I am a simple chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot:", random.choice(responses["goodbye"]))
            break
        print("Chatbot:", chatbot_response(user_input))

# Start chatting
chat()
