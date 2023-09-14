#!/usr/bin/python3
"""module that lists states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           password=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.name\
                From cities INNER JOIN states \
                ON states.id = cities.state_id \
                WHERE states.name = %s \
                ORDER BY cities.id ASC", (sys.argv[4],))
    query_rows = cur.fetchall()
    cities_list = list(row[0] for row in query_rows)
    print(*cities_list, sep=", ")
    cur.close()
    conn.close()
