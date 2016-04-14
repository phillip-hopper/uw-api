import psycopg2
from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('../.settings/uw-publishing.cfg')


def connect_db():
    """
    :return: psycopg2.Connection
    """
    return psycopg2.connect("dbname=test user=postgres")


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    print app.config['DATABASE']
    app.run()
