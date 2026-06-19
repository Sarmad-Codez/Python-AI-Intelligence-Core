import re
import time

def get_ai_response(user_input):
    # Normalize input: lowercase and remove extra characters
    user_input = user_input.lower().strip()
    
    # Define keywords dictionary for mapping intent
    responses = {
        r'(hello|hi|hey|assalam|aoa)': 
            "Walaikum Assalam / Hello! I am your AI Assistant. How can I help you with code or logic today? 🤖",
            
        r'(how are you|how is it going|khairiyat)': 
            "Alhamdulillah, I am running at peak processing speed! How are things on your side? ⚡",
            
        r'(what is your name|who are you|introduce)': 
            "I am a Rule-Based AI Chatbot prototype, built to demonstrate context recognition and NLP logic. 🔍",
            
        r'(python|c\+\+|programming|coding)': 
            "Programming is all about logic! Python is beautiful for AI/ML, while C++ is king for performance. What are you building?",
            
        r'(ai|machine learning|artificial intelligence|ml)': 
            "AI is the future! It allows machines to learn from data patterns rather than explicit hardcoded rules. Exciting field to master! 🚀",
            
        r'(github|portfolio|repository)': 
            "A clean GitHub portfolio with distinct file names separates clean engineers from hobbyists. Keep pushing commits! 💻",
            
        r'(bye|exit|allah hafiz|tc)': 
            "Allah Hafiz! Take care, human. Shutting down subroutines... 👋"
    }

    # Match input against intents using regex (Regular Expressions)
    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response
            
    # Default response if AI doesn't recognize the specific keywords
    return "🧠 Interesting point. I am still expanding my keyword matrix. Could you rephrase that or ask about AI/Programming?"

def start_bot():
    print("="*50)
    print("        RULE-BASED AI CONTEXT CHATBOT         ")
    print("="*50)
    print("AI: System online. Type 'exit' or 'Allah Hafiz' to quit.\n")
    
    while True:
        user_text = input("You: ")
        
        # Check for exit condition before parsing
        if any(word in user_text.lower() for word in ['exit', 'bye', 'allah hafiz']):
            print("\nAI: Allah Hafiz! Have a productive day. 🚀")
            break
            
        print("AI is thinking...", end="\r")
        time.sleep(0.4)  # Simulating processing latency
        
        bot_reply = get_ai_response(user_text)
        print(f"AI: {bot_reply}\n")

if __name__ == "__main__":
    start_bot()