#!/usr/bin/python3
""" Script that takes argument and displays all values in states table of
database hbtn_0e_0_usa where name matches argument. """


import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    search_state = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name, charset="utf8")
    cs = db.cursor()

    query = ("SELECT * FROM states WHERE name LIKE BINARY '{}'"
             "ORDER BY id ASC".format(search_state))
    cs.execute(query)
    rows = cs.fetchall()
    for row in rows:
        print(row)

    cs.close()
    db.close()
