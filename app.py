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

@app.route('/db_create')
def creating():
    conn = psycopg.connect('postgresql://flasklab_user:BkBajs8ePSBumCOTvAlLqOTRd9gQhbYe@dpg-d24pmt7gi27c73ba47rg-a/flasklab')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First varchar(255),
            Last varchar(255),
            City varchar(255),
            Name varchar(255),
            Number int
            );
    ''')
    conn.commit()
    conn.close()
    return 'Basketball Table Successfully Created'

@app.route('/db_insert')
def inserting():
    conn = psycopg.connect('postgresql://flasklab_user:BkBajs8ePSBumCOTvAlLqOTRd9gQhbYe@dpg-d24pmt7gi27c73ba47rg-a/flasklab')
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return 'Basketball Table Successfully Populated'

@app.route('/db_select')
def selecting():
    conn = psycopg.connect('postgresql://flasklab_user:BkBajs8ePSBumCOTvAlLqOTRd9gQhbYe@dpg-d24pmt7gi27c73ba47rg-a/flasklab')
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM Basketball;
    ''')
    records = cur.fetchall()
    conn.close()
    response_string = ''
    response_string += '<table>'
    for player in records:
        response_string += '<tr>'
        for info in player:
            response_string += "<td>{}</td>".format(info)
        response_string += '</tr>'
    response_string += '</table>'
    return response_string

@app.route('/db_drop')
def dropping():
    conn = psycopg.connect('postgresql://flasklab_user:BkBajs8ePSBumCOTvAlLqOTRd9gQhbYe@dpg-d24pmt7gi27c73ba47rg-a/flasklab')
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE Basketball;
    ''')
    conn.commit()
    conn.close()
    return 'Basketball Table Successfully Dropped'