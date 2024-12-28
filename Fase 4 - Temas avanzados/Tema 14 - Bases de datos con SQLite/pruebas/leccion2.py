import sqlite3

conexion = sqlite3.connect("productos.db")
cursor = conexion.cursor()

"""cursor.execute( '''
    CREATE TABLE usuarios (
               dni VARCHAR(9) PRIMARY KEY ,
               nombre VARCHAR(100),
               edad INTEGER,
                email VARCHAR(100)
    )
''')

personas = [
    ( "11111111a","Mario", 45, "mario@ejemplo.com"),
    ( "22222222b", "juan", 25, "juan@ejemplo.com"),
    ( "33333333c", "josefa", 15, "juana@ejemplo.com"),
    ( "44444444d", "sebastian", 20, "sebas@ejemplo.com"),
    ( "55555555e", "arely", 19, "arely@ejemplo.com"),

]"""

# cursor.execute("INSERT INTO usuarios VALUES ( "11111111a","Mario", 45, "mario@ejemplo.com")")
# cursor.executemany("INSERT INTO usuarios VALUES (?,?,?,?)",personas)

#campos autoincrementales
"""
cursor.execute('''
    CREATE TABLE productos( 
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre VARCHAR(100) NOT NULL,
               marca VARCHAR(100) NOT NULL,
               precio FLOAT NOT NULL
    )
               ''')
"""
# productos = [
        # ("pantalla logitech", "logitech",1233),
        # ("pantalla asus", "asus",1033)
# ]
cursor.execute("SELECT * FROM productos")
productos = cursor.fetchall()
print(productos)
# cursor.executemany("INSERT INTO productos VALUES(null, ?,?,?)",productos)
conexion.commit()
conexion.close()