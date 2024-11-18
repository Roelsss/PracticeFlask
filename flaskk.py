from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name="Flask Developer")

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/about')
def about():
    return "This is the About Page!"

@app.route('/contact')
def contact():
    return "This is the Contact Page"

@app.route('/user/<username>')
def show_user_profile(username):
    return f"Hello, {username}!"

if __name__ == '__main__':
    app.run(debug=True)