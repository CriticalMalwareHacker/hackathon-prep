
from flask import Flask, redirect, request, render_template, flash, session, url_for, jsonify
import os
import yfinance as yf
import requests  # Import the requests library

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return redirect(url_for('contact'))
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form_type = request.form.get('form_type')

        if form_type == 'signup':
            email = request.form['email']
            password = request.form['password']
            confirm_password = request.form['confirm_password']
            if password == confirm_password:
                session['registered_email'] = email
                session['registered_password'] = password
                flash("Account has been successfully created. Please log in.", "success")
            else:
                flash("Passwords do not match. Please try again.", "error")
            return redirect(url_for('login'))

        elif form_type == 'login':
            email = request.form['email']
            password = request.form['password']
            if email == session.get('registered_email') and password == session.get('registered_password'):
                return redirect(url_for('dashboard'))
            else:
                flash("Invalid credentials, please try again.")
    return render_template('login.html', prefilled_email=session.get('registered_email'))

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    symbol = 'AAPL'  # Default symbol
    if request.method == 'POST':
        symbol = request.form['symbol'].upper()
    
    market_data = get_market_data(symbol)
    return render_template('dashboard.html', market_data=market_data, symbol=symbol)

@app.route('/chatbot', methods=['GET'])  # New route for the chatbot page
def chatbot():
    return render_template('genai.html')  # Render the chatbot interface

@app.route('/get_chatbot_response', methods=['POST'])  # New route for chatbot responses
def get_chatbot_response_route():
    user_input = request.json.get('input')
    print(f"User input received: {user_input}")  # Debugging print
    response_text = get_chatbot_response(user_input)
    print(f"Chatbot response: {response_text}")  # Debugging print
    return jsonify({'response': response_text})

def get_chatbot_response(user_input):
    url = 'https://your.actual.api.endpoint'  # Replace with your actual API URL
    headers = {'Authorization': f'Bearer AlzaSyDhXXtAcScaClhF_nwh7Kid1x_yyrrd6M', 'Content-Type': 'application/json'}
    data = {'input': user_input}

    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            print("Successful response from API")  # Debugging print
            return response.json().get('response', "No response key found")  # Adjust if needed
        else:
            print(f"API Error: Status Code {response.status_code}")
            return "I'm sorry, but I can't answer that right now."
    except Exception as e:
        print(f"Exception occurred: {e}")
        return "I'm sorry, there was an error processing your request."

@app.route('/logout')
def logout():
    session.pop('registered_email', None)
    session.pop('registered_password', None)
    return redirect(url_for('home'))

def get_market_data(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="5d")  # Get historical data for the last 5 days
    return data

if __name__ == '__main__':
    app.run(debug=True)
