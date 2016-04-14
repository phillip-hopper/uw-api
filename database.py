import psycopg2

db = psycopg2.connect(database=app.config['DATABASE'],
                      user=app.config['DATABASE'],
                      password=app.config['DATABASE'],
                      host=app.config['DATABASE'])
