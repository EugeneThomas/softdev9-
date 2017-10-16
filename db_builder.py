# Eugene Thomas
# SoftDev1 pd7
# HW09 -- No Treble
# 2017-10-16

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

file1 = open('peeps.csv')
d1 = csv.DictReader(file1)
file2 = open('courses.csv')
d2 = csv.DictReader(file2)
f="discobandit.db"
db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

command = "CREATE TABLE STUDENTS(NAME TEXT, AGE INTEGER, ID INTEGER)"
c.execute(command)    #run SQL statement
command = "CREATE TABLE COURSES(CODE TEXT, MARK INTEGER, ID INTEGER)"
c.execute(command)    #run SQL statement
for row in d1:
    name = row['name']
    age = row['age']
    Id = row['id']
    command = "INSERT INTO STUDENTS VALUES('" + name + "', " + age + ", " + Id + ")"
    c.execute(command) #run SQL statement
for row in d2:
    name = row['code']
    age = row['mark']
    Id = row['id']
    command = "INSERT INTO STUDENTS VALUES('" + name + "', " + age + ", " + Id + ")"
    c.execute(command) #run SQL statement
#==========================================================
db.commit() #save changes
db.close()  #close database
