#!/usr/bin/python3
""" Script that takes argument and displays all values in states table of
database hbtn_0e_0_usa where name matches argument. _safe_ """

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cs = db.cursor()
    match = sys.argv[4]
    cs.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))

    rows = cs.fetchall()
    for row in rows:
        print(row)

    cs.close()
    db.close()
