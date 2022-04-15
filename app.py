from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    html = "<h1>Welcome! This is Udacity Capstone Project For Cloud DevOps Engineer Nanodegree Program V1</h1>"
    return html.format(format)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)