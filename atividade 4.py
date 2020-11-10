for i in range(0,10):
    listaNumeros = int(input("numero: "))
    numeros_pares = [i for i in range(10) if not i % 2]
    numeros_impar = [i for i in range(10) if  i % 2]
print("numeros par",numeros_pares)
print("numeros impar",numeros_impar)