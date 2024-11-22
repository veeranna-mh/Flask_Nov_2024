from flask import Flask, request
import pickle

app=Flask(__name__)

model_file = open("classifier.pkl", "rb")
model = pickle.load(model_file)

# model.predict(inputs)

# lets create end points

@app.route('/',method=["GET"])
def home():
    return "<h1>Loan Approval Application</h1>"

@app.route('/predict',method=["GET","POST"])
def predict():
    if request.method=="POST":
        #do prediction
        pass
    else:
        return "<h2>I will make the prediction</h2>"