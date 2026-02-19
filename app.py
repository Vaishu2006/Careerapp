from flask import Flask, render_template, request
from logic.career_engine import (
    career_after_10th,
    career_after_12th,
    career_after_engineering,
    medical_specialization,
    govt_careers
)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

# -------- AFTER 10TH --------
@app.route("/flow/10th")
def after10th():
    return render_template("after10th.html")

@app.route("/result/10th", methods=["POST"])
def result10th():
    choices = request.form.get("choices")
    careers = career_after_10th(choices)
    return render_template("result.html", careers=careers)

# -------- AFTER 12TH --------
@app.route("/flow/12th")
def after12th():
    return render_template("after12th.html")

@app.route("/result/12th", methods=["POST"])
def result12th():
    stream = request.form.get("stream")
    careers = career_after_12th(stream)
    return render_template("result.html", careers=careers)

# -------- ENGINEERING --------
@app.route("/flow/engineering")
def engineering():
    return render_template("engineering.html")

@app.route("/result/engineering", methods=["POST"])
def result_engineering():
    branch = request.form.get("branch")
    interest = request.form.get("interest")
    careers = career_after_engineering(branch, interest)
    return render_template("result.html", careers=careers)

# -------- MEDICAL --------
@app.route("/flow/medical")
def medical():
    return render_template("medical.html")

@app.route("/result/medical", methods=["POST"])
def result_medical():
    interest = request.form.get("interest")
    careers = medical_specialization(interest)
    return render_template("result.html", careers=careers)

# -------- EXPLORE --------
@app.route("/flow/explore")
def explore():
    return render_template("explore.html")

@app.route("/result/explore", methods=["POST"])
def result_explore():
    interest = request.form.get("interest")
    careers = govt_careers(interest)
    return render_template("result.html", careers=careers)
if __name__ == "__main__":
    app.run()

