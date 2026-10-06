from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("software_risk_model.pkl")

# -----------------------------
# Load dataset to get columns
# -----------------------------
df = pd.read_csv("OnlyTrivial_dt.csv")
df = df.select_dtypes(include=['number'])
df['risk_level'] = 0

columns = df.drop('risk_level', axis=1).columns

risk_map = {
    0: "Low Risk",
    1: "Medium Risk",
    2: "High Risk"
}

# -----------------------------
# Home Page
# -----------------------------
@app.route('/')
def home():
    return render_template("home.html")


# -----------------------------
# About Page
# -----------------------------
@app.route('/about')
def about():
    return render_template("about.html")


# -----------------------------
# Predict Page
# -----------------------------
@app.route('/predict')
def predict():
    return render_template("predict.html")


# -----------------------------
# Result Page
# -----------------------------
@app.route('/result', methods=['POST'])
def result():

    input_data = {col:0 for col in columns}

    input_data['cbo'] = float(request.form['cbo'])
    input_data['fanin'] = float(request.form['fanin'])
    input_data['fanout'] = float(request.form['fanout'])
    input_data['wmc'] = float(request.form['wmc'])
    input_data['dit'] = float(request.form['dit'])
    input_data['noc'] = float(request.form['noc'])
    input_data['rfc'] = float(request.form['rfc'])
    input_data['lcom'] = float(request.form['lcom'])
    input_data['loc'] = float(request.form['loc'])
    input_data['loopQty'] = float(request.form['loopQty'])
    input_data['comparisonsQty'] = float(request.form['comparisonsQty'])
    input_data['maxNestedBlocksQty'] = float(request.form['maxNestedBlocksQty'])

    data = pd.DataFrame([input_data])
    data = data[columns]

    prediction = model.predict(data)[0]
    prob = model.predict_proba(data)[0]

    labels = ["Low Risk", "Medium Risk", "High Risk"]

    return render_template(
        "result.html",
        prediction=risk_map[prediction],
        labels=labels,
        prob=prob.tolist()
    )


# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)