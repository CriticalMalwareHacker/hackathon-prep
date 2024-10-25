from flask import Flask, request, render_template, flash
from models import recommend_investment, handle_user_query

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

# Route for the homepage
@app.route('/')
def home():
    return render_template('main.html')

# Route to handle user input for recommendations
@app.route('/recommend', methods=['POST'])
def get_recommendations():
    user_age = request.form.get('age')
    user_income = request.form.get('income')
    user_goals = request.form.get('goals')
    risk_tolerance = request.form.get('risk_tolerance')

    # Input validation
    if not user_age.isdigit() or not user_income.isdigit():
        flash("Please enter valid numeric values for age and income.")
        return render_template('main.html')

    # Pass data to the recommendation function
    recommendations = recommend_investment(user_age, user_income, user_goals, risk_tolerance)

    # Check if recommendations were returned
    if not recommendations:
        flash("No recommendations could be generated. Please try again.")
        return render_template('main.html')

    # Render a new template to show the recommendations
    return render_template('recommendations.html', recommendations=recommendations)

# Route to handle chat queries
@app.route('/chat', methods=['POST'])
def chat():
    user_query = request.form.get('query')
    response = handle_user_query(user_query)

    # Flashing the response for better user experience
    flash(f"Chatbot Response: {response}")
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)