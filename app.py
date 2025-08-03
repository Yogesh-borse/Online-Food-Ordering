# app.py (Flask Application)
from flask import Flask

app = Flask()

@app.route('/')
def home():
    return "<h1>Welcome to Yogesh Madhukar Borse's Website</h1><p>Flask application with Nginx & Gunicorn</p>"

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)