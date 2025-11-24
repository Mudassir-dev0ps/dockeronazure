from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Jenkins → Docker Hub → Azure VM 🎉 second try"

app.run(host="0.0.0.0", port=5000)
