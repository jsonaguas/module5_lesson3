from main import connect_database
from mysql.connector import Error
def view_members():
    conn = connect_database()
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM members')
            rows = cursor.fetchall()
            for row in rows:
                print(row) 
        finally:
            conn.close()
            cursor.close()