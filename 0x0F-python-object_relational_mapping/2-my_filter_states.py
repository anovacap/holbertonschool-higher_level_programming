#!/usr/bin/python3
"""takes in an argument and displays all values in the states table
 of hbtn_0e_0_usa where name matches the argument"""
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
    cur.execute("SELECT * FROM states WHERE name = '{}'".format(argv[4]))

    for row in cur.fetchall():
        print(row)
    db.close()

if __name__ == "__main__":
    import sys
    main(sys.argv)
