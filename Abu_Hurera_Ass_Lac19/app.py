from flask import Flask, render_template, request

app = Flask(__name__)

# --- Home Route ---
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username and password:
            message = f"Welcome, {username}!"
        else:
            message = "Error: Both username and password are required!"
    return render_template('login.html', message=message)

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        return render_template('feedback_result.html', name=name, email=email, message=message)
    return render_template('feedback.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        return render_template('submit.html', method="POST")
    else:
        return render_template('submit.html', method="GET")

if __name__ == '__main__':
    app.run(debug=True)
