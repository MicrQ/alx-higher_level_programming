#!/usr/bin/python3
""" a script that takes in arguments and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument.
    safe from sql injection
"""

if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    """ necessary modules """

    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM `states` \
    WHERE BINARY `name` = %s ORDER BY id", (argv[4],))

    [print(row) for row in cur.fetchall()]
