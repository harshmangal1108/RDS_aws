#!/usr/bin/python3
import mysql.connector as mysql


#        RDS INFO
un='root'

pd='*****'

db='harsh'

ht='something'


# NOW CONNECTING

conn=mysql.connect(user=un,password=pd,database=db,host=ht)


#NOW GENERATING SQL LANGUAGE CURSOR

cur=conn.cursor()


# NOW WE CAN WRITE SQL QUERY

cur.execute("show tables;")

cur.execute("select * from dockers;")

# TO PRINT OUTPUT
print(cur.fetchall())


# CLOSE DATABASE CONNECTION
conn.close()

