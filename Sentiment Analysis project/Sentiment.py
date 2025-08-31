# Import the required library
from textblob import TextBlob

# Function to analyze sentiment
def analyze_sentiment(text):
    # Create a TextBlob object
    analysis = TextBlob(text)
    
    # Get the sentiment polarity (-1 to 1)
    polarity = analysis.sentiment.polarity
    
    # Determine sentiment based on polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Main program
print("Welcome to Simple Sentiment Analysis Tool!")
print("Enter 'quit' to exit the program.")

while True:
    # Get user input
    user_text = input("\nEnter text to analyze: ")
    
    # Check if user wants to quit
    if user_text.lower() == 'quit':
        print("Thank you for using the Sentiment Analysis Tool!")
        break
    
    # Analyze the sentiment
    sentiment = analyze_sentiment(user_text)
    
    # Display the result
    print(f"Sentiment: {sentiment}")