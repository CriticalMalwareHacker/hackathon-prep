from flask import Flask, redirect, request, render_template, flash, session, url_for, jsonify

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages

# Mock database for users
user_db = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Process contact form data if needed
        return redirect(url_for('contact'))  # Redirect to prevent form resubmission
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
            
            # Check if the user is registered
            if email != session.get('registered_email'):
                flash("Email not found. Please sign up.", "info")
                return redirect(url_for('login'))
            
            # Login logic
            if email == session.get('registered_email') and password == session.get('registered_password'):
                return redirect(url_for('dashboard'))
            else:
                flash("Invalid credentials, please try again.", "error")

    return render_template('login.html', prefilled_email=session.get('registered_email'))

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    # Clear the session to log out the user
    session.pop('registered_email', None)
    session.pop('registered_password', None)
    return redirect(url_for('home'))

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()  # Get JSON data
    user_query = data.get('query')  # Access the user's query
    response = generate_response(user_query)
    return jsonify({'response': response})  # Return JSON response for AJAX

def generate_response(user_query):
    # You can keep this function or modify it as needed.
    # Placeholder for chat response generation.
    return "This is a placeholder response."

if __name__ == '__main__':
    app.run(debug=True)
