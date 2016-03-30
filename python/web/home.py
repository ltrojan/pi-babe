import flask

app = flask.Flask(__name__)


@app.route('/greet/<name>/')
def greet(name):
    return flask.render_template('greet.html', name=name)


@app.route('/')
def home():
    return flask.render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
