import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

#Create two tables
c.execute('CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER)' )
c.execute('CREATE TABLE peeps(name TEXT, age INTEGER, id INTEGER)' )

#Insert data
with open('courses.csv') as csvfile:
    grade = csv.DictReader(csvfile)
    for row in grade:
        c.execute('INSERT INTO courses VALUES (?, ?, ?)', (row['code'], row['mark'], row['id']))

with open('peeps.csv') as csvfile:
    name = csv.DictReader(csvfile)
    for row in name:
        c.execute('INSERT INTO peeps VALUES (?, ?, ?)', (row['name'], row['age'], row['id']))

#==========================================================
db.commit() #save changes
db.close()  #close database


