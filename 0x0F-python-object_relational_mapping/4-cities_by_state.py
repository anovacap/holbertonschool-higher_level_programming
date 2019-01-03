#!/usr/bin/python3
"""lists all cities from the database"""
import MySQLdb
import sys


def main(argv):
    """func - main - argv"""
    if len(argv) != 4:
        print("Enter 3 arguments")
        return

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN "
                "states ON cities.state_id = states.id")

    for row in cur.fetchall():
        print(row)
    db.close()

if __name__ == "__main__":
    import sys
    main(sys.argv)
