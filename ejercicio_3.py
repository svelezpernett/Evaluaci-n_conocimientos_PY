# -Construir un programa para ir de compras en un supermercado que permita la construcción del siguiente MENU:
# 1. Digitar 1 para recibir {código, nombre, precio} de un producto(+0.4) 
# 2. Digitar 2 para mostrar todos los productos registrados (+0.4)
# 3. Digitar 3 para permitir buscar por código un producto y editar el precio
# de este (+0.4)
# 4. Digitar 4 para permitir buscar por código un producto y eliminar el
# producto (+0.4)
# 5. Digitar 0 para SALIR


opcion =int((input("Ingrese el numero 1 para añadir producto: ")))
productos_registrados=[]
if opcion ==1 :
    while (opcion !="*"):
        codigo= int(input("ingrese el codigo del articulo "))
        nombre= input("ingrese el nombre del articulo ")
        precio= float(input("ingrese el valor del articulo "))
        producto ={'nombre':nombre, 'codigo':codigo, 'precio':precio}
        productos_registrados.append(producto)
        opcion =(input("Ingrese * para terminar de ingresar productos, o culquier tecla para seguir añadiendo: "))
    opcion =int((input("Ingrese el numero 2 para ver los productos: ")))
if opcion==2 :
    print(productos_registrados)
    opcion =int((input("Ingrese el numero 3 para buscar por codigo y modificar: ")))
if opcion==3 :
    codigo_buscar=int(input("Ingrese el codigo del producto a consultar : "))
    for producto in productos_registrados:
        if codigo_buscar == (producto['codigo']):
            print(producto['codigo'], producto['nombre'], producto['precio'])
            seleccion_para_cambio=int((input("1, para combiar codigo, 2 para cambiar nombre, y 3 para cambiar precio, y 4 paraeliminar el producto ")))
            if seleccion_para_cambio == 1:
                codigo_nuevo=int(input("Ingrese el nuevo codigo: "))
                producto['codigo'] = codigo_nuevo
                print(producto)
                print("Cambio guardado con exito!")
                opcion =int((input("Ingrese el numero 1 para ingresar un nuevo producto, 2 para ver los productos o 3 para buscar ymodificar productos")))
            if seleccion_para_cambio == 2:
                nombre_nuevo=input("Ingrese el nuevo nombre: ")
                producto['nombre'] = nombre_nuevo
                print(producto)
                print("Cambio guardado con exito!")
                opcion =int((input("Ingrese el numero 1 para ingresar un nuevo producto, 2 para ver los productos o 3 para buscar ymodificar productos")))
            if seleccion_para_cambio == 3:
                precio_nuevo=int(input("Ingrese el precio codigo: "))
                producto['precio'] = precio_nuevo
                print(producto)
                print("Cambio guardado con exito!")
                opcion =int((input("Ingrese el numero 1 para ingresar un nuevo producto, 2 para ver los productos o 3 para buscar ymodificar productos")))
            if seleccion_para_cambio == 4:
                del(productos_registrados[producto])
                print("producto eliminado con exito!")
                opcion =int((input("Ingrese el numero 1 para ingresar un nuevo producto")))
            print(producto['codigo'], producto['nombre'], producto['precio'])
        if opcion == 9:
            exit()



