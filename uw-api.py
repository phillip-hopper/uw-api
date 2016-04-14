from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('../.settings/uw-api.cfg')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    print app.config['DATABASE']
    app.run()
