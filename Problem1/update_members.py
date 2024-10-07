from main import connect_database
from mysql.connector import Error

def update_members(id, name, age):
    query = 'UPDATE Members SET name = %s, age = %s WHERE id = %s'
    cursor.execute(query, (name, age, id))

conn = connect_database()
if conn is not None:
    try:
        cursor=conn.cursor()
        member_id = 7
        check_query = 'SELECT id FROM Members WHERE id = %s'
        cursor.execute(check_query, (member_id,))
        member = cursor.fetchone()

        if member is None:
            print('Member does not exist')
            exit()
        
        if member:
            update_members(7, 'Gertrude', 36)
            conn.commit()
            print('Member updated')
    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn and conn.is_connected():
            conn.close()
            cursor.close()