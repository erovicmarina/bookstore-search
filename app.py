from flask import Flask

app = Flask(__name__)
@app.route("/") 

def home():
    return "Svako dobro dobri ljudi"

if __name__ == "__main__":
    app.run(debug=True)
