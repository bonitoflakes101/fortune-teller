from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "HELLOOO WORLDDD"

if __name__ == '__main__':
    app.run(debug=True)
