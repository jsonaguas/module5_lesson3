from main import connect_database
from mysql.connector import Error

def delete_members(id):
    query = 'DELETE FROM Members WHERE id = %s'
    cursor.execute(query, (id,))

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()
        member_id = 9
        check_query = 'SELECT id FROM Members WHERE id = %s'
        cursor.execute(check_query, (member_id,))
        member = cursor.fetchone()

        if member is None:
            print('Member does not exist')
            exit()
        
        if member:
            delete_members(9)
            conn.commit()
            print('Member deleted')
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn and conn.is_connected():
            conn.close()
            cursor.close()
            