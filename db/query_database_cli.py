import sqlite3
import argparse

"""
python .\query_database.py --query "Select * from users"
python .\query_database.py --file .\query.sql

"""


def query_database(query: str):
    # Connect to the SQLite database
    conn = sqlite3.connect('../test.db')

    # Create a cursor object
    cur = conn.cursor()

    # Execute a query
    cur.execute(query)  # Replace with your table name and query

    # Fetch all rows of a query result
    rows = cur.fetchall()

    # Iterate and print the rows
    for row in rows:
        print(row)

    # Close the connection
    conn.close()


def main():
    parser = argparse.ArgumentParser(description='Query the SQLite database.')
    parser.add_argument('--query', help='SQL query to execute')
    parser.add_argument('--file', help='Path to SQL file to execute')
    
    args = parser.parse_args()

    if args.query:
        query_database(args.query)
    elif args.file:
        with open(args.file, 'r') as f:
            query_database(f.read())
    else:
        print("No query or file provided")

if __name__ == "__main__":
    main()