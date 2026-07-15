"""
This lab will explore establishing a database connection via Python and SQLite,
as well as creating a table, inserting data, and selecting that data.
"""
import sqlite3


conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

def __main__():
    insert_dog('Mister', 'Foxhound', 5)

# Create a dogs table with autoincrementing ID
def create_dogs_table():
    cursor.execute('''
        CREATE TABLE dogs(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(20),
            breed VARCHAR(20),
            age INTEGER
        );
    ''')



# TODO: Complete insert_dog() by inserting a new dog (provided in the parameters) into the "dogs" table.
def insert_dog(name, breed, age):

    cursor.execute('''INSERT INTO dogs (name, breed, age) VALUES (?, ?, ?)''', (name, breed, age))


# TODO: Complete select_all_dogs() by selecting all rows from the "dogs" table *and returning them*.
def select_all_dogs():

    # return the rows
    cursor.execute('''SELECT * FROM dogs''')
    return cursor.fetchall()

if __name__ == '__main__':
    create_dogs_table()
    insert_dog('Mister', 'Foxhound', 5)
    print(select_all_dogs())



