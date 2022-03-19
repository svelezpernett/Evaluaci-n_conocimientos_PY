# -Construir un programa que permita ingresar N (cantidad digitada por el
# usuario) números enteros y cuente cuantos múltiplos de 2 y de 3 fueron
# ingresados (+1)

numerosLista=[]
multiplos_3 =[]
multiplos_2 =[]
tamano=int(input("Ingrese el tamaño de la lista:"))

for i in range(tamano):
    numero=int(input("Ingrese el número de la lista:"))
    numerosLista.append(numero)
for num in numerosLista:
    if num %3==0 and num%2==0:
        multiplos_3.extend([num])
        multiplos_2.extend([num]) 
    elif num %3 ==0 :
        multiplos_3.extend([num])
    elif num%2 ==0 :
        multiplos_2.extend([num])
    
print ("los numeros ingresados son ", numerosLista)    
print("la cantidad de multiplos de 3 es : ",len(multiplos_3))
print("la cantidad de multiplos de 2 es : ",len(multiplos_2))


