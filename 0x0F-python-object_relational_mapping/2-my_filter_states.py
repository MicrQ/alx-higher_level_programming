#!/usr/bin/python3
"""  a script that takes in an argument and displays all values
    in the states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
from sys import argv as av

if __name__ == "__main__":
    """ necessary modules """

    db = MySQLdb.connect(user=av[1], passwd=av[2], db=av[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM `states` \
    WHERE `name` LIKE BINARY '{}' ORDER BY id ASC".format(av[4]))

    [print(row) for row in cur.fetchall()]
