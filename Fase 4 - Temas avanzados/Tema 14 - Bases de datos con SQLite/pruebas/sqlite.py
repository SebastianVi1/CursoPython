import sqlite3

conexion = sqlite3.connect("ejemplo.db")#creamos un archivo sql
cursor = conexion.cursor()#creamos un cursor

#creamos una tabla para usuarios
# cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))") 

#agregamos info a los campos
#cursor.execute("INSERT INTO usuarios VALUES ('Sebastian', 20, 'sebastian@gmail.com')")

#recuperar la informacion de un usuario
# cursor.execute("SELECT * FROM usuarios")
# usuario = cursor.fetchone()
# print(usuario)

#insertor multiples usuarios
#personas = [
 #   ("Mario", 45, "mario@ejemplo.com"),
  #  ("juan", 25, "juan@ejemplo.com"),
   # ("josefa", 15, "juana@ejemplo.com"),
#]
# cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", personas)

cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

for i in usuarios:
    print(i)

conexion.commit()
conexion.close()
