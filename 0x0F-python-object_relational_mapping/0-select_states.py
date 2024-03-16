#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa """

from sys import argv
import MySQLdb
""" Importing the necessary modules """

db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])

cur = db.cursor()

cur.execute('SELECT * FROM `states` ORDER BY `id` ASC')
for row in cur.fetchall():
    print(row)
