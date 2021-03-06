#!/usr/bin/python3
"""
   This module contains a MySQLdb query.
"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    USER = argv[1]
    PSWD = argv[2]
    DB = argv[3]

    db = MySQLdb.connect(user=USER, host="localhost", db=DB, passwd=PSWD)
    cur = db.cursor()

    cur.execute("""SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id\
    ASC""")
    rows = cur.fetchall()

    for row in rows:
        if row[1][0].isupper():
            print(row)

    cur.close()
    db.close()
