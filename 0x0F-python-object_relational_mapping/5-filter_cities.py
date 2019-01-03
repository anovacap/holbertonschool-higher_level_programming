#!/usr/bin/python3
"""Ltakes in the name of a state as an argument and lists all
 cities of that state,"""
import MySQLdb
import sys


def main(argv):
    """func - main - argv"""
    if len(argv) != 5:
        print("Enter 4 arguments")
        return

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities JOIN states ON cities."
                "state_id = states.id WHERE states.name=%s", (argv[4],))

    print(", ".join([row[0] for row in cur]))
    db.close()

if __name__ == "__main__":
    import sys
    main(sys.argv)
