import mysql.connector


def run_query(query):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sql123",
        database="employees"
    )

    cursor = connection.cursor()
    cursor.execute(query)

    for row in cursor:
        print(row)

    cursor.close()
    connection.close()


run_query(
    "SELECT emp_no, first_name, last_name "
    "FROM employees LIMIT 10"
)