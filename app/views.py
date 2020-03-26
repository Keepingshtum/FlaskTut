from app import app
from flask import render_template,url_for
@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/about")
def about():
    return """
    <h1 style='color: red;'>I'm a red H1 heading!</h1>
    <p>This is a lovely little paragraph</p>
    <code>Flask is <em>awesome</em></code>
    """

@app.route("/upload.php",methods=['POST'])
def upload():
    return url_for('static',filename='upload.php')