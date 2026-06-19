import time

def classify_message(message):
    message = message.lower().strip()
    
    # Core spam trigger words/phrases matrix
    spam_indicators = [
        'win money', 'free prize', 'click here', 'lottery', 'cash bonus', 
        'earn money fast', 'crypto double', 'urgent download', 'claim offer', 
        'congratulations free', 'winner', 'subscribe now', 'investment profit'
    ]
    
    spam_score = 0
    triggered_words = []
    
    # Check for direct phrase hits or keyword combinations
    for indicator in spam_indicators:
        if indicator in message:
            spam_score += 2
            triggered_words.append(indicator)
            
    # Additional risk analysis for text patterns
    if '!' in message and spam_score > 0:
        spam_score += 1  # Urgency mark increases spam probability
        
    print("\n[AI Security Subroutine: Scanning Message Headers...]")
    time.sleep(0.4)
    
    print(f"🕵️  Risk Analysis Score: {spam_score} | Flags Triggered: {triggered_words}")
    
    # Threshold classification logic
    if spam_score >= 2:
        return "🚨 Status: SPAM DETECTED! (High probability of fraud/ad phishing.)"
    else:
        return "✅ Status: HAM / SECURE (Message is clean.)"

def main():
    print("="*50)
    print("         AI BINARY SPAM CLASSIFIER            ")
    print("="*50)
    print("Type 'exit' to shut down the filter network.\n")
    
    while True:
        user_msg = input("Enter incoming message/email text: ").strip()
        
        if user_msg.lower() == 'exit':
            print("\nDeactivating spam filter shield. Allah Hafiz! 🛡️")
            break
            
        if not user_msg:
            print("❌ Input network stream empty!")
            continue
            
        classification = classify_message(user_msg)
        print(f"➡️ {classification}\n")
        print("-" * 50)

if __name__ == "__main__":
    main()