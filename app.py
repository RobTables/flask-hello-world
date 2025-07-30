from flask import Flask
import psycopg
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Andrew in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg.connect('postgresql://flasklab_user:BkBajs8ePSBumCOTvAlLqOTRd9gQhbYe@dpg-d24pmt7gi27c73ba47rg-a/flasklab')
    conn.close()
    return 'Database Connection Successful'