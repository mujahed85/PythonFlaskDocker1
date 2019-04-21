import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>This is H1 Tag</h1><p>This is P tag in HTML.</p>"

app.run()