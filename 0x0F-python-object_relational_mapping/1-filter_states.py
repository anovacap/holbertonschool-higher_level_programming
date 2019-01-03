#!/usr/bin/python3
"""lists all states with a name starting with N"""
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
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    for row in cur.fetchall():
        print(row)
    db.close()

if __name__ == "__main__":
    import sys
    main(sys.argv)
