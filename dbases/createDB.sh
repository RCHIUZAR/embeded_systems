#!/bin/bash

# MariaDB server connection details
DB_USER="your_db_user"        # Replace with your MariaDB username
DB_PASSWORD="your_db_password"  # Replace with your MariaDB password
DB_HOST="localhost"           # Change if your database is on a different host
DB_NAME="sensor2023"          # Name of the database you want to create

# SQL commands to create the database and table
SQL_CREATE_DB="CREATE DATABASE IF NOT EXISTS $DB_NAME;"  # Create the database if it doesn't exist

# Define SQL to create the table 'sensor' with specific columns
SQL_CREATE_TABLE="USE $DB_NAME;
                 CREATE TABLE IF NOT EXISTS sensor (
                     s_ID INT AUTO_INCREMENT PRIMARY KEY,  # Auto-incrementing ID
                     s_date DATE,                         # Date column
                     s_time TIME,                         # Time column
                     s_temp FLOAT,                       # Temperature column (floating-point)
                     s_hum FLOAT                         # Humidity column (floating-point)
                 );"

# Execute SQL commands to create the database and table
mysql -u"$DB_USER" -p"$DB_PASSWORD" -h "$DB_HOST" -e "$SQL_CREATE_DB"
mysql -u"$DB_USER" -p"$DB_PASSWORD" -h "$DB_HOST" -e "$SQL_CREATE_TABLE"

# Check the exit status of the MySQL commands
if [ $? -eq 0 ]; then
    echo "Database and table created successfully."
else
    echo "Error creating the database and table."
fi


