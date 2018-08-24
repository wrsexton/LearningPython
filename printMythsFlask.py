import sqlite3
from sqlite3 import Error

from flask import Flask
app = Flask(__name__)

@app.route('/')
def print_myths():
    # create connection
    con = sqlite3.connect('myths.db')
    # get cursor
    c = con.cursor()

    textReturn = '''
    <h2>Mythical creatures: </h2>
    <ul>
    '''

    # print data
    for row in c.execute('SELECT name, description FROM myths ORDER BY name').fetchall():
        textReturn = textReturn + ('<li>{0}  --  {1}</li>'.format(row[0], row[1]))

    textReturn = textReturn + '</ul>'
    # close connection
    con.close()
    return textReturn
