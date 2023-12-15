#!/usr/bin/python3
""" Script that lists all cities from database hbtn_0e_0_usa. """


import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name, charset="utf8")
    cs = db.cursor()

    cs.execute("""SELECT cities.name FROM cities
               INNER JOIN states ON states.id=cities.state_id
               WHERE states.name=%s""", (sys.argv[4],))
    rows = cs.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")

    cs.close()
    db.close()
