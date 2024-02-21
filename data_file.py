import sqlite3

# Establish a connection
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# Query all data
cursor.execute("SELECT * FROM events WHERE date='2088.10.15'")
print(cursor.fetchall())

# Qeury certain data
cursor.execute("SELECT band,date FROM events WHERE date='2088.10.15'")
print(cursor.fetchall())

# #Inser new rows
# new_rows = [('Dimond', 'Dimond City', '2088.12.15'),
#             ('`Arsen`', 'Arsen City', '2088.11.15')]
#
# cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
# connection.commit()

#Show all data
cursor.execute("SELECT * FROM events")
print(cursor.fetchall())