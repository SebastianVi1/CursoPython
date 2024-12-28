import sqlite3

def agregar_categoria():
    try:
        categoria = input("Ingrese el nombre de la categoría para añadirla: ")
        conexion = sqlite3.connect("restaurante.db")
        cursor = conexion.cursor()

        # Utilizamos parámetros en la consulta SQL para evitar la inyección de SQL
        cursor.execute("INSERT INTO categoria (nombre) VALUES (?)", (categoria,))

        conexion.commit()
        print("Categoría creada exitosamente.")
    except sqlite3.IntegrityError:
        print("La categoría ya existe.")
    except sqlite3.Error as e:
        print("Error al agregar la categoría:", e)
    finally:
        conexion.close()

# Crear la base de datos antes de entrar al bucle principal


while True:
    print("__BIENVENIDO AL SISTEMA__")
    print("1.- Crear una categoría")
    print("2.- Salir")       
    op = input("Elija una opción: ")
    if op == "1":
        agregar_categoria()
    elif op == "2":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
