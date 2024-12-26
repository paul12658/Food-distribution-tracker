from flask import Flask, jsonify, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_scss import Scss
from dotenv import load_dotenv
import os
from enum import Enum

app = Flask(__name__)
Scss(app)

# Load environment variables from the .env file
load_dotenv()

# Configure SQLAlchemy to use the MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"mysql+mysqlconnector://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

# Disable tracking modifications to save resources
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask application
db = SQLAlchemy(app)



#  the root URL returns a welcome message
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')  # Render your login template

if __name__ == "__main__":
    app.run(debug=True)
