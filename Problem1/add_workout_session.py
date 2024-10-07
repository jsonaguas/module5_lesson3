from main import connect_database
from mysql.connector import Error

def add_workout(session_id, member_id, session_date, session_time, activity):
    cursor.execute('SELECT id FROM Members WHERE id = %s', (member_id,))
    result = cursor.fetchone()
    
    if result:
        query = 'INSERT INTO WorkoutSessions (session_id, member_id, session_date, session_time, activity) VALUES (%s, %s, %s, %s, %s)'
        cursor.execute(query, (session_id, member_id, session_date, session_time, activity))
        return True
    else:
        print(f"Error: member_id {member_id} does not exist in the Members table")
        return False


conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()
        success = add_workout(7,6,'2024-10-03','0700','basektball')
        if success:
            conn.commit()
            print('New workout session added')
        else:
            print('No workout session added')

    except Error as e:
        print(f"Error: {e}")
    finally:
        if conn and conn.is_connected():
            conn.close()
            cursor.close()
