
print("podemos declarar conjuntos atravez da funcao set ")
numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}

print("ou podemos declarar conjuntos atravez de chaves")
nomes = {"joao","paulo"}
print(nomes)

print("""
não podemos acessar um indice do conjunto ,
entao temos que transformar ele primeiro em uma lista
      """)
numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0])

print("""
para saber se algum elemento esta contido em um conjunto
usamos a palavra reservada (in).""")

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

print("utilizamos union para somar os dos conjuntos em ul so")
conjunto_a = {1, 2}
conjunto_b = {3, 4}

resultado = conjunto_a.union(conjunto_b)
print(resultado)


print("utilizamos intersection para pegar os numeros que se repetem nos dois conjuntos")
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.intersection(conjunto_b)
print(resultado)# 2,3

print("utilizamos difference para saber o que um conjunto tem de diferente do outro")
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.difference(conjunto_b)
print(resultado)

resultado = conjunto_b.difference(conjunto_a)
print(resultado)

print("utilizamos symmetric_diference para saber o que tem de diferente em anbos os conjuntos")
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.symmetric_difference(conjunto_b)
print(resultado)

print("utilizamos issubset para saber se um conjunto esta contido em outro ou nao")
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issubset(conjunto_b)  # True
print(resultado)

resultado = conjunto_b.issubset(conjunto_a)  # False
print(resultado)

print("utilizamos isdisjoint para saber se um elemento  nao se repete em outro conjunto")
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

resultado = conjunto_a.isdisjoint(conjunto_b)  # True
print(resultado)

resultado = conjunto_a.isdisjoint(conjunto_c)  # False
print(resultado)

print("utilizamos add para inserir um elemento no conjunto")
sorteio = {1, 23}

sorteio.add(25)  # {1, 23, 25}
print(sorteio)

sorteio.add(42)  # {1, 23, 25, 42}
print(sorteio)

sorteio.add(25)  # {1, 23, 25, 42}
print(sorteio)

print("utilizamos clear para linpar um conjunto")
sorteio = {1, 23}

print(sorteio)  # {1,23}

sorteio.clear()

print(sorteio)  # {}

print("utilizamos copy para criar um novo conjunto apartir de um existente")
sorteio = {1, 23}

print(sorteio)  # {1, 23}

novoConjunto = sorteio.copy()

print(novoConjunto)  # {1, 23}
sorteio.add(3)
print(sorteio)

print("utilizamos discard para eliminar um elemento do conjunto")
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.discard(1)
numeros.discard(45)

print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9, 0}

print("utilizamos pop para eliminar o elemento do indice zero do conjunto")
numeros = {0,1,2,3}
print(numeros)
numeros.pop()
print(numeros)
numeros.pop()
print(numeros)



print("utilizamos remove para remover um elemento do conjunto")
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 19, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.remove(19))  # 0
print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

print("utilizamos len para saber quantos elementos tem no conjunto")
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(len(numeros))  # 10

print("utilizamos in para saber se o elemento esta contido no conjunto")
numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(1 in numeros)  # True
print(10 in numeros)  # False