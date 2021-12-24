# 1. Import Flask
from flask import Flask 

# 2. Create an app
app = Flask(__name__)

# 3. Define index route
@app.route('/')
def home():
    return (f'Hello world!\n'
    f'Welcome to my API')

# 4. Define the about route
@app.route("/about")
def about():
    name = 'Byron'
    location = 'Toronto'
    return f'My name is {name} and I live in {location}'

# 5. Define the contact route
@app.route('/contact')
def contact():
    email = 'byronkrauskopf@gmail.com'
    return f'I can be rached at {email}'

# 6. Define main behavior
if __name__ == '__main__':
    app.run(debug=True)