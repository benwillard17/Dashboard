#/usr/bin/python2.4 #
import psycopg2
import sys

# Connect with Database
try:
    conn = psycopg2.connect("dbname='CHF_Homepage' user='postgres' host='localhost' password='password'")
    print("Opened database successfully")
except:
    print("Connected to the database")

cur = conn.cursor()

# Drop all tables from a given database
try:
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cur.execute("""DROP DATABASE CHF_Homepage""")
    print("CHF_Homepage database dropped!")
except:
    print("I can't drop the CHF_Homepage database!")


