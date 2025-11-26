from flask import Flask, request, \
    render_template

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.form["data"]
        return f"Method POST: {data}"
    
    return render_template("index.html")
