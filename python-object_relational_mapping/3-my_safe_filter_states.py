#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states table
where name matches the argument (safe from SQL injection)
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query with parameterized input
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all rows
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the cursor and connection
    cursor.close()
    db.close()
