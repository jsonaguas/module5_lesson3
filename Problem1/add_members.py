from main import connect_database
from mysql.connector import Error
from view_members import view_members

def add_members(member_id,name,age):
    query = 'INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)'
    cursor.execute(query, (member_id, name, age))

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()
        add_members(8, 'Hephaestus', 60)
        conn.commit()
        print('New member(s) added')
        view_members()

    except Error as e:
        if e.errno == 1062:  # Error code for duplicate entry
            print(f"Error: Duplicate entry for id")
        else:
            print(f"Error: {e}")
    finally:
        if conn and conn.is_connected():
            conn.close()
            cursor.close()