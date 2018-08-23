#!/usr/bin/env python3

import sqlite3
from sqlite3 import Error

# create connection
con = sqlite3.connect('myths.db')
# get cursor
c = con.cursor()

# create database if it doesn't exist, print error if it does
try:
    c.execute('''
    CREATE TABLE myths
    (name text)
    ''')
except Error as e:
    print('\nReady to enter some more mythical creatures?\n')#(e)

# collect mythical creature data from user and store in database
mythName = ''
while mythName.lower() != 'q':
    mythName = input("Enter a cool mythical creature (q to quit): ")
    if mythName.lower() != 'q':
        c.execute('''
        INSERT INTO myths VALUES ('{}')
        '''.format(mythName))

# save data
con.commit()

print("\nLook at all of these mythical creatures you know: ")

# print data
for row in c.execute('SELECT * FROM myths').fetchall():
    print(row)

# close connection
con.close()