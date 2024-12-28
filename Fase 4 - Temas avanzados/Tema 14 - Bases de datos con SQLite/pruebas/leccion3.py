import sqlite3

conexion = sqlite3.connect("users.db")
cursor = conexion.cursor()

cursor.execute("SELECT * FROM users1 WHERE dni='11111111a'")
usuario = cursor.fetchone()
print(usuario)

# cursor.execute("UPDATE users1 SET nombre='Sebastian' WHERE id=4")#cambiar campo de un registro
cursor.execute("DELETE FROM users1 WHERE id='1'")
conexion.commit()
conexion.close()