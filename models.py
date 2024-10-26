"""import pandas as pd
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
"""
# models.py

# This file can be used for database models if you're using a database
# For simplicity, I have left it empty as you might not have specific models yet.

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

# Add other models as needed...
