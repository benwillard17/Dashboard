import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'test_dmp.settings'
import django; django.setup()
from django.contrib.auth import models as conmod
import homepage.models as hmod
from django.contrib.auth.models import Group, Permission, ContentType
import psycopg2
import sys


# Connect with Database
try:
    conn = psycopg2.connect("dbname='CHF_Homepage' user='postgres' host='localhost' password='satoko5286'")
    print("Opened database successfully")
    conn.set_isolation_level(0)
except:
    print("Connected to the database")

cur = conn.cursor()

# Drop all tables from a given database
try:
    cur.execute("SELECT table_schema,table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_schema,table_name")
    rows = cur.fetchall()
    for row in rows:
        print("dropping table: ", row[1])
        cur.execute("drop table " + row[1] + " cascade")
    cur.close()
    conn.close()
    print("All tables dropped from CHF_Homepage.")
except:
    print("Error: ", sys.exc_info()[1])
