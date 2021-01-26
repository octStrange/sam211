from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Welcome to Flask <a href="/home">Click Here</a>'
    
@app.route('/home')
def index():
    return 'Home page'

if __name__ == "__main__":
    app.run(debug=True)
