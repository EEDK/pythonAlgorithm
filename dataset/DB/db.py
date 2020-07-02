#https://yes90.tistory.com/57
import sqlite3

conn = sqlite3.connect('company.db')
curs = conn.cursor()

curs.execute("insert into employee values('lee','28')")
conn.commit()