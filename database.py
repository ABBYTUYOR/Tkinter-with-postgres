from tkinter import messagebox

import psycopg2
import tkinter
HOSTNAME = "localhost"
DATABASE = "personal_data"
USERNAME = "postgres"
PASSWORD = 1234
PORT = 5432

conn = None
cur = None
def database_connect():
    return psycopg2.connect(host=HOSTNAME, dbname=DATABASE, user=USERNAME, password=PASSWORD, port=PORT)


def database_table_create():
    with database_connect() as conn:
        with conn.cursor() as cur:
            create_script = """
                                CREATE TABLE IF NOT EXISTS info (
                                    id SERIAL PRIMARY KEY,
                                    fname VARCHAR(25) NOT NULL,
                                    mname VARCHAR(25) NOT NULL,
                                    lname VARCHAR(25) NOT NULL
                                )
                            """
            cur.execute(create_script)


def database_save(fname, mname, lname):
    if len(fname) == 0 or len(mname) == 0 or len(lname) == 0:
        messagebox.showinfo("Error", "Please fill all required fields")
    else:
        with database_connect() as conn:
            with conn.cursor() as cur:
                insert_script = "INSERT INTO info (fname, mname, lname) VALUES (%s, %s, %s)"
                insert_values = (fname, mname, lname)
                cur.execute(insert_script, insert_values)
                if cur.rowcount > 0 :
                    messagebox.showinfo("Success", "Saved ")


def database_update(fname, mname, lname):
    if len(fname) == 0 or len(mname) == 0 or len(lname) == 0:
        messagebox.showinfo("Error", "Please fill all required fields")
    else:
        with database_connect() as conn:
            with conn.cursor() as cur:
                update_script = "UPDATE info SET fname = %s, mname = %s, lname = %s WHERE fname = %s"
                update_values = (fname, mname, lname, fname)
                cur.execute(update_script, update_values)
                if cur.rowcount > 0 :
                    messagebox.showinfo("Success", "Updated ")

def database_delete(fname):
    if len(fname) == 0:
        messagebox.showinfo("Error", "Please fill all required fields")
    else:
        with database_connect() as conn:
            with conn.cursor() as cur:
                delete_script = "DELETE FROM info WHERE fname = %s "
                delete_values = (fname,)
                cur.execute(delete_script, delete_values)
                if cur.rowcount > 0 :
                    messagebox.showinfo("Success", "Deleted ")

def database_display():
    with database_connect() as conn:
        with conn.cursor() as cur:
            select_script = "SELECT * FROM info"
            cur.execute(select_script)
            for row in cur.fetchall():
                print(row[1], row[2], row[3])

            print("--------------")







