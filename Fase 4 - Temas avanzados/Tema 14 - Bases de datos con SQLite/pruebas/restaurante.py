import sqlite3

def crear_db():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("""
                CREATE TABLE categoria(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre VARCHAR(100) UNIQUE NOT NULL)
                    """)
        cursor.execute("""
                CREATE TABLE plato(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre VARCHAR(100) UNIQUE NOT NULL, 
                categoria_id INTEGER NOT NULL,
                FOREIGN KEY(categoria_id) REFERENCES categoria(id))       
                       """)
    except:
        print("La base de datos ya ha sido creada")
    conexion.commit()
    conexion.close()

def agregar_categoria():
   
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    try:
        categoria = input("ingrese el nombre de la categoria para anadirla: ")
        #creamos una catergoria nueva
        cursor.execute("INSERT INTO categoria VALUES (null, '{}')".format(categoria))
        
        conexion.commit()
        print("Categoria creada exitosamente")
        
    except:
        print("la categoria ya ha sido creada")
    finally:
       conexion.close()

def agregar_plato():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM categoria")
    categorias = cursor.fetchall()
    
    print("Elige una categoria")
    for cat in categorias:
        print("{}.-Categoria: {}".format(cat[0], cat[1]))
    op = int(input(">"))
    plato =input("Nombre del plato para agregar: ")
    try:
        #creamos una catergoria nueva
        cursor.execute("INSERT INTO plato VALUES (null, '{}', '{}')".format(plato, op))
        
        conexion.commit()
        print("Plato agregado exitosamente")
  
    except sqlite3.IntegrityError:
        print("El plato {} ya existe".format(plato))


    conexion.commit()
    conexion.close()

def mostrar_menu():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM categoria")
    categorias = cursor.fetchall()

    

    print("\t \t__MENU__")
    cont = 0
    for i in categorias:
        print("categoria: {}".format(i[1]))
        platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(i[0])).fetchall()
        for plato in platos:
            cont +=1
            print(" \t{}- Plato: {}".format(cont, plato[1]))
    conexion.close()



while True:
    
    print("__BIENVENIDO AL SISTEMA--")
    print("1.-Crear una categoria")
    print("2.-Agregar un plato") 
    print("3.-Mostrar menu")  
    print("4.-Salir")     
    op = input(">")
    if op == "1":
        agregar_categoria()
    if op == "2":
        agregar_plato()
    if op == "3":
        mostrar_menu()
    if op == "4":
        break
    else:
        pass


