import sqlite3

def create_db():
    conn = sqlite3.connect('school.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS Account(ID INTEGER PRIMARY KEY ,'
                'name TEXT ,username TEXT,'
                'password TEXT) ')
    conn.commit()
    cur.execute('CREATE TABLE IF NOT EXISTS Admin(admin_ID INTEGER PRIMARY KEY ,'
                'admin_name TEXT ,admin_username TEXT,'
                'admin_password TEXT) ')
    conn.commit()
create_db()
