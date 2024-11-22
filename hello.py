from flask import Flask
app=Flask(__name__)
# lets create end points

@app.route('/')
def home():
    return "<h1>Flask API</h1>"

@app.route('/ping')
def pinger():
    return {"message" : "Hello there!!!"}


