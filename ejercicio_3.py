# -Construir un programa para ir de compras en un supermercado que permita la construcción del siguiente MENU:
# 1. Digitar 1 para recibir {código, nombre, precio} de un producto(+0.4) 
# 2. Digitar 2 para mostrar todos los productos registrados (+0.4)
# 3. Digitar 3 para permitir buscar por código un producto y editar el precio
# de este (+0.4)
# 4. Digitar 4 para permitir buscar por código un producto y eliminar el
# producto (+0.4)
# 5. Digitar 0 para SALIR


opcion =int((input("Ingrese la opcion: ")))
productos_registrados=[]
if opcion ==1 :
    while (opcion !="*"):
        codigo= int(input("ingrese el codigo del articulo "))
        nombre= input("ingrese el nombre del articulo ")
        precio= float(input("ingrese el valor del articulo "))
        producto ={'nombre':nombre, 'codigo':codigo, 'precio':precio}
        productos_registrados.append(producto)
        opcion =(input("Ingrese * para terminar de ingresaar producto: "))
    opcion =int((input("Ingrese la opcion: ")))
if opcion==2 :
    print(productos_registrados)
    opcion =int((input("Ingrese la opcion 3 para bucar por codigo y modificar: ")))
if opcion==3 :
    codigo_buscar=int(input("Ingrese el codigo del producto a consultar : "))
    if codigo_buscar==productos_registrados(producto['codigo']):
        print("melo")
