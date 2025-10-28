from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Route 1: /hello/<username>
@app.route('/hello/<username>')
def hello_user(username):
    return render_template('hello.html', name=username)

# Route 2: /welcome
@app.route('/welcome')
def welcome():
    return "<h2>Welcome to the Flask App! 🎉</h2>"

# Route 3: /square/<int:number>
@app.route('/square/<int:number>')
def square(number):
    result = number ** 2
    return f"<h3>The square of {number} is {result}</h3>"

# Route 4: /repeat/<string:word>/<int:times>
@app.route('/repeat/<string:word>/<int:times>')
def repeat_word(word, times):
    return f"<p>{(word + ' ') * times}</p>"

# Route 5: /info (current date and time)
@app.route('/info')
def info():
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return f"<h3>Current Date and Time: {formatted_time}</h3>"

if __name__ == '__main__':
    app.run(debug=True)
