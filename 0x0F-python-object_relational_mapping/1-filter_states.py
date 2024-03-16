#!/usr/bin/python3
""" a script that lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv
""" Importing necessary modules """

if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()

    stmt = "SELECt * FROM `states` WHERE `name` LIKE 'N%' ORDER BY `id` ASC"
    cur.execute(stmt)
    for row in cur.fetchall():
        print(row)
