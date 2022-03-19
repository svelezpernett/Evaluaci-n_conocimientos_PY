# -Leer el nombre de 10 frutas para preparar un salpicón; el programa debe
# permitir mostrar las 10 frutas ingresadas al mismo tiempo en sentido
# inverso al ingresado+(1)
print("escriba 'ya' si desea terminar de añadir elementos ")
lista_frutas=[]
fruta=(input("Ingrese la fruta:"))
while (fruta != "ya"):
    lista_frutas.append(fruta)
    fruta=(input("Ingrese la fruta:"))
lista_frutas.reverse()
print(lista_frutas)