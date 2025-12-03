from flask import Flask, request, \
    render_template

app = Flask(__name__)


images = [
    "image_01",
    "image_02",
    "image_11", 
    "image_12", 
    "image_15",
    "image_27", 
    "image_37",
]

@app.route('/', methods=["GET"])
def home_get():
    # print(request.args.get("img"))
    image = request.args.get("img")
    if image in images:
        image = "images/" + image + ".jpg"
    else:
        image = None
    return render_template("index.html", images=images, image=image)

@app.route('/', methods=["POST"])
def home_post():
    data = request.form["data"]
    return f"Method POST: {data}"
