import sqlite3


def access():
    conn = sqlite3.connect(puppylab.db);
    cur = conn.cursor()
    cur.execute("SELECT Type from EmployersID")
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
