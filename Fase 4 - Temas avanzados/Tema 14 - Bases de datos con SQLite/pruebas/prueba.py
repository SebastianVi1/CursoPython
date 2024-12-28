import sqlite3

conexion = sqlite3.connect("users.db")
cursor = conexion.cursor()
"""
cursor.execute('''
        CREATE TABLE users1 (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               dni VARCHAR(100) UNIQUE,
               nombre VARCHAR(100),
               telefono VARCHAR(20)
        )
               ''')
"""

datos = [
    ( "11111111a","Mario", "67876653"),
    ( "22222222b", "juan", "23452342"),
    ( "33333333c", "josefa", "23423424"),
    ( "44444444d", "sebastian", "234234"),
    ( "55555555e", "arely", "234235234")
]

cursor.executemany("INSERT INTO users1 VALUES (null,?,?,?)",datos)

conexion.commit()
conexion.close()