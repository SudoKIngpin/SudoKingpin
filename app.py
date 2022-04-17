from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ContactMe')
def contact():
    return render_template('contact.html')

@app.route('/robots.txt')
def robot():
    return render_template('/robots.txt')

@app.route('/magic')

def magic():
    return render_template('button.htm')
# app.run(debug=True)


