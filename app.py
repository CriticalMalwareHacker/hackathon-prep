from flask import Flask, render_template, request
from models import recommend_investment, handle_user_query

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle user input for recommendations
@app.route('/recommend', methods=['POST'])
def get_recommendations():
    # Get form data like user age, income, or preferences
    user_age = request.form.get('age')
    user_income = request.form.get('income')
    user_goals = request.form.get('goals')
    risk_tolerance = request.form.get('risk_tolerance')

    # Pass data to the recommendation function
    recommendations = recommend_investment(user_age, user_income, user_goals, risk_tolerance)

    # Render a new template to show the recommendations
    return render_template('recommendations.html', recommendations=recommendations)

# Route to handle chat queries
@app.route('/chat', methods=['POST'])
def chat():
    user_query = request.form.get('query')
    response = handle_user_query(user_query)
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
