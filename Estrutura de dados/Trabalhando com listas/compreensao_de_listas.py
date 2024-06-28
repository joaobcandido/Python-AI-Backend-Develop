# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
# passando os 2 argumentos obrigatorios e um if opcional
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
# passando os 2 argumentos obrigatorios 
quadrado = [numero**2 for numero in numeros]
print(quadrado)