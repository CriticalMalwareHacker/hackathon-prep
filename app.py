from flask import Flask, redirect, request, render_template, flash, session, url_for, jsonify
import yfinance as yf

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
                flash("Passwords do not match. Please try again.")
            return redirect(url_for('login'))

        elif form_type == 'login':
            email = request.form['email']
            password = request.form['password']
            if email == session.get('registered_email') and password == session.get('registered_password'):
                session['user_email'] = email  # Store user email in session
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
    recommendation = None  # Placeholder for recommendations
    reason = None          # Placeholder for the reason of recommendation
    return render_template('dashboard.html', market_data=market_data, symbol=symbol, recommendation=recommendation, reason=reason)

@app.route('/logout')
def logout():
    session.pop('user_email', None)  # Remove user email from session
    session.pop('registered_email', None)
    session.pop('registered_password', None)
    return redirect(url_for('home'))

def get_market_data(symbol):
    stock = yf.Ticker(symbol)
    data = stock.history(period="5d")  # Get historical data for the last 5 days
    return data.to_dict(orient='index')  # Convert to dictionary for easier rendering


if __name__ == '__main__':
    app.run(debug=True)
