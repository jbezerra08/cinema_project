from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_word():
    #a = 1 / 0
    return "Hello World"

if __name__ == "__main__":
    app.run(debug = True)

