from main import connect_database   
from mysql.connector import Error

def between_ages(start_age,end_age):
    query = 'SELECT * FROM Members WHERE age BETWEEN %s AND %s'
    cursor.execute(query, (start_age, end_age))

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()
        between_ages(30, 40)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn and conn.is_connected():
            conn.close()
            cursor.close()