from flask import Flask
app = Flask(__name__)

@app.route('/')
def aboutMe():
    return 'Hello, Iam mohamed nazeer fullstack (python django) ...'