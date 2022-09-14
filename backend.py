import sqlite3

def connect():
    connected = sqlite3.connect("Phones_Record.db")
    cur= connected.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS phonerecord (id INTEGER PRIMARY KEY, phone_name TEXT, camera TEXT, launch_date DATE, battery TEXT, display_size TEXT, price FLOAT)")
    connected.commit()
    connected.close()

def insert(phone_name, camera, launch_date, battery, display_size, price):
    connected = sqlite3.connect("Phones_Record.db")
    cur= connected.cursor()
    cur.execute("INSERT INTO phonerecord VALUES (NULL, ?,?,?,?,?,?)",(phone_name, camera, launch_date, battery, display_size, price))
    connected.commit()
    connected.close()

def view():
    connected = sqlite3.connect("Phones_Record.db")
    cur= connected.cursor()
    cur.execute("SELECT * FROM phonerecord")
    rows=cur.fetchall()
    connected.close()
    return rows

def search(phone_name="", camera="", launch_date="", battery="", display_size="", price=""):
    connected = sqlite3.connect("Phones_Record.db")
    cur= connected.cursor()
    cur.execute("SELECT * FROM phonerecord WHERE phone_name=? OR camera=? OR launch_date=? OR battery=? OR display_size=? OR price=?",(phone_name, camera, launch_date, battery, display_size, price))
    rows=cur.fetchall()
    connected.close()
    return rows

def delete(id):
    connected = sqlite3.connect("Phones_Record.db")
    cur= connected.cursor()
    cur.execute("DELETE FROM phonerecord WHERE id=?",(id,))
    connected.commit()
    connected.close()

def update(id,phone_name, camera, launch_date, battery, display_size, price):
    connected = sqlite3.connect("Phones_Record.db")
    cur= connected.cursor()
    cur.execute("UPDATE phonerecord SET phone_name=?,camera=?, launch_date=?, battery=?, display_size=?, price=? WHERE id=?",(phone_name, camera, launch_date, battery, display_size, price, id))
    connected.commit()
    connected.close()


connect()
#print(search(camera="48MP"))
#delete(None)
#update(4, "IPHONE 12", "45MP", "2020-10-12", "4000mAH", "6.1inch", 507.89)
#insert("IPHONE 13","32MP","2021-12-15","4000mAH", "6.2inch", 769.99 )
#print(view())
