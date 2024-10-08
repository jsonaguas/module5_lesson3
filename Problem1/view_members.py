from main import connect_database
from mysql.connector import Error

def view_members(cursor):
    conn = connect_database()
    if conn is not None:
        print('Members:')
        try:
            cursor = conn.cursor()
            query = 'SELECT * FROM Members'
            cursor.execute(query)
            rows = cursor.fetchall()
            if rows:
                for row in rows:
                    print(row) 
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                conn.close()
                cursor.close()
    return cursor

