import sqlite3


def access():
    connector = sqlite3.connect("puppylab.db")
    cur = connector.cursor()
    cur.execute("SELECT Type FROM EmployersID")
    rows = cur.fetchall()
    print(rows)

access()


