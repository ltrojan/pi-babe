from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return flask.render_template('index.html')


if _name__ == "__main__":
    app.run(debug=True)
