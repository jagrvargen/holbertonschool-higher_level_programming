#!/usr/bin/env python3
"""
   This module contains a MySQLdb query.
"""
import MySQLdb
from sys import argv


USER = argv[1]
PSWD = argv[2]
DB = argv[3]
NAME = argv[4]

db = MySQLdb.connect(user=USER, host="localhost", db=DB, passwd=PSWD)
cur = db.cursor()

cur.execute("""SELECT cities.name FROM cities, states WHERE cities.state_id = states.id AND states.name = %s  ORDER BY cities.id ASC""", (NAME,))
rows = cur.fetchall()

city_list = []
for city in rows:
    city_list.append(city[0])

for i in range(len(city_list) - 1):
    print(city_list[i], end="")
    print(", ", end="")

print(city_list[-1])

cur.close()
db.close()
