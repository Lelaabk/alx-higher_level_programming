#!/usr/bin/python3
""" Script that lists all states from database hbtn_0e_0_usa. """


import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1];
    password = sys.argv[2];
    db_name = sys.argv[3];

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name, charset="utf8")
    cs = db.cursor();

    query = "SELECT * FROM states ORDER BY id ASC"
    cs.execute(query);
    rows = cs.fetchall()
    for row in rows:
        print(row)

    cs.close()
    db.close()
