from flask import Flask
app = Flask(__name__)
@app.route("/ping")
def ping():
#    return "pong..."
    return "pong...BUT NOW WITH ERROR"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)