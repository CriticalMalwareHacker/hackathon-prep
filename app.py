from flask import Flask, render_template, url_for

app=Flask(__name__)

@app.route('/')#makes sure you get the content ur intended to get and doesnt show a 404 error page
def index():
    return render_template('main.html')

if __name__=="__main__":
    app.run(debug=True)#we get to know errors we need to set debug to false