import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the required NLTK data once (comment this out after the first run)
nltk.download('vader_lexicon')

# Initialize the Sentiment Analyzer
sia = SentimentIntensityAnalyzer()

# Dummy function to simulate recommendation logic
def recommend_investment(age, income, goals, risk_tolerance):
    # Replace with real recommendation logic or use mock data for now.
    recommendations = ["Stock A", "Stock B", "Crypto C"]
    if risk_tolerance == "low":
        recommendations = ["Bonds", "Fixed Deposits", "Mutual Funds"]
    elif risk_tolerance == "medium":
        recommendations = ["Blue Chip Stocks", "Balanced Mutual Funds"]
    elif risk_tolerance == "high":
        recommendations = ["Crypto", "Small Cap Stocks", "Real Estate"]
    return recommendations

# Function to handle user queries using NLTK for sentiment analysis
def handle_user_query(query):
    sentiment = sia.polarity_scores(query)
    if sentiment['compound'] >= 0.05:
        return "It seems you're optimistic. Stocks might be a good choice!"
    elif sentiment['compound'] <= -0.05:
        return "It looks like you're a bit cautious. Perhaps consider safer investments like bonds."
    else:
        return "It's always a good idea to review your financial goals before making a decision."
