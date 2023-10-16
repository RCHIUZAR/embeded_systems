#!/usr/bin/python3
"""
Designed by R. Chiu for the embeded system lecture.
(r)2023  Universidad de Guadalajara MX
All the code comments where gerenerated automatically by chatGPT 3.5
"""


import pymysql  # Import the pymysql library for working with MySQL databases
from datetime import datetime
from random import seed
from random import random
import time

# Connect to the MySQL database
db = pymysql.connect(host='localhost', user='pi3', passwd='emb2023', db='sensor2023')
cur = db.cursor()

# Get the current date and time
now = datetime.now()
year = now.year
month = now.month
day = now.day

hour = now.hour
minute = now.minute
second = now.second

# Generate random values for temperature and humidity
ran1 = random()
ran2 = random()

# Format the date and time as strings
s_date = "{0}-{1}-{2}".format(year, month, day)
s_time = "{0}:{1}:{2}".format(hour, minute, second)

# Format the random values for temperature and humidity with 2 decimal places
s_temp = "{:.2f}".format(ran1)
s_hum = "{:.2f}".format(ran2)

# Create an SQL query to insert data into the 'sensor' table
q1 = "INSERT INTO sensor VALUES(NULL, '{0}', '{1}', '{2}', '{3}')".format(s_date, s_time, s_temp, s_hum)

# Execute the SQL query
cur.execute(q1)

# Commit the changes to the database
db.commit()

# Close the database connection
db.close()

