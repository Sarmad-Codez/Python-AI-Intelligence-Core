import time

def analyze_sentiment(text):
    # Lowercase text to match keywords easily
    text = text.lower().strip()
    
    # Positive word matrix
    positive_words = [
        'good', 'great', 'awesome', 'amazing', 'love', 'happy', 'best', 
        'excellent', 'nice', 'perfect', 'brilliant', 'productive', 'maza', 'behtareen'
    ]
    
    # Negative word matrix
    negative_words = [
        'bad', 'worst', 'hate', 'sad', 'angry', 'terrible', 'error', 'fail', 
        'wrong', 'useless', 'boring', 'rubbish', 'waste', 'ganda', 'masla'
    ]
    
    pos_score = 0
    neg_score = 0
    
    # Split text into single words to score them
    words = text.split()
    
    for word in words:
        # Clean word from punctuation if any
        clean_word = ''.join(e for e in word if e.isalnum())
        if clean_word in positive_words:
            pos_score += 1
        elif clean_word in negative_words:
            neg_score += 1
            
    # Logic to determine final sentiment
    print("\n[AI Processing Analysis...]")
    time.sleep(0.3)
    print(f"📊 Scores -> Positive Tokens: {pos_score} | Negative Tokens: {neg_score}")
    
    if pos_score > neg_score:
        return "✨ Sentiment: POSITIVE (User seems happy/satisfied!)"
    elif neg_score > pos_score:
        return "❌ Sentiment: NEGATIVE (User seems disappointed/frustrated!)"
    else:
        return "😐 Sentiment: NEUTRAL (Normal statement or mixed signals.)"

def main():
    print("="*50)
    print("         AI TEXT SENTIMENT ANALYZER           ")
    print("="*50)
    print("Type 'exit' to close the analyzer.\n")
    
    while True:
        user_sentence = input("Enter a sentence/review to analyze: ").strip()
        
        if user_sentence.lower() == 'exit':
            print("\nShutting down NLP analyzer. Allah Hafiz! 📊")
            break
            
        if not user_sentence:
            print("❌ Input cannot be empty!")
            continue
            
        result = analyze_sentiment(user_sentence)
        print(f"➡️ {result}\n")
        print("-" * 50)

if __name__ == "__main__":
    main()