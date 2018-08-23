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
    (name text, description text)
    ''')
except Error as e:
    print('\nReady to enter some more mythical creatures?\n')#(e)

# collect mythical creature data from user and store in database
mythName = ''
mythDesc = ''
while mythName.lower() != 'q':
    mythName = input("Enter a cool mythical creature (q to quit): ")
    if mythName.lower() == 'q':
        break
    if not mythName:
        print("You didn't enter anything!")
        continue
    mythDesc = input("Describe that mythical creature: ")
    c.execute('''
    INSERT INTO myths (name, description) VALUES ('{0}', '{1}')
    '''.format(mythName, mythDesc))

# save data
con.commit()

print("\nLook at all of these mythical creatures you know: \n")

# print data
for row in c.execute('SELECT name, description FROM myths ORDER BY name').fetchall():
    print('|  {0}  --  {1}'.format(row[0], row[1]))

# close connection
con.close()
