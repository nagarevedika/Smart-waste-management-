from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report", methods=["POST"])
def report():
    location = request.form.get("location")
    issue = request.form.get("issue")
    return f"Report received! Location: {location}, Issue: {issue}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
