from flask import Flask, redirect, request, render_template, flash, session, url_for
import os
import google.generativeai as genai

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

# Configure the API key from environment variable
genai.configure(api_key=os.environ["API_KEY"])

# Mock database for users
user_db = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form_type = request.form.get('form_type')

        if form_type == 'signup':
            email = request.form['email']
            password = request.form['password']
            confirm_password = request.form['confirm_password']
            
            # Signup logic
            if password == confirm_password:
                # Store credentials in session for demonstration purposes
                session['registered_email'] = email
                session['registered_password'] = password
                flash("Account has been successfully created. Please log in.", "success")
            else:
                flash("Passwords do not match. Please try again.", "error")
            return redirect(url_for('login'))

        elif form_type == 'login':
            email = request.form['email']
            password = request.form['password']
            
            # Login logic
            if email == session.get('registered_email') and password == session.get('registered_password'):
                return redirect(url_for('dashboard'))
            else:
                flash("Invalid credentials, please try again.", "error")

    return render_template('login.html', prefilled_email=session.get('registered_email'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_query = request.form.get('query')
    response = generate_response(user_query)
    return render_template('home.html', user_query=user_query, bot_response=response)

def generate_response(user_query):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(user_query)
    return response.text

if __name__ == '__main__':
    app.run(debug=True)
