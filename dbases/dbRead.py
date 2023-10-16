#!/usr/bin/python3
"""
Designed by R. Chiu for the embeded system lecture.
(r)2023  Universidad de Guadalajara MX
All the code comments where gerenerated automatically by chatGPT 3.5
"""

import pymysql

# Database connection parameters
host = 'localhost'  # Change to your MySQL server host
user = 'pi3'        # Change to your MySQL username
password = 'emb2023'  # Change to your MySQL password
database = 'sensor2023'  # Change to your database name

# Connect to the MySQL database
db = pymysql.connect(host=host, user=user, password=password, db=database)

try:
    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # SQL query to select all data from the 'sensor' table
    sql_query = "SELECT * FROM sensor;"

    # Execute the SQL query
    cursor.execute(sql_query)

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Print the table header
    print("s_id\t  s_date\t    s_time\t  s_temp\t  s_hum")
    print("-" * 45)

    # Iterate through the rows and print each row's data
    for row in rows:
        s_id, s_date, s_time, s_temp, s_hum = row
        print(f"{s_id}\t  {s_date}\t  {s_time}\t  {s_temp}\t  {s_hum}")

except Exception as e:
    print(f"Error: {e}")

finally:
    # Close the cursor and database connection
    cursor.close()
    db.close()
