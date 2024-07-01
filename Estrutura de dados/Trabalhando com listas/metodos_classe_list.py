print("""
 append
 utilizamos o append inserir um elemento dentro de uma lista
""")
lista = [1,2]
print(lista)
lista.append(3)
print(lista)
lista.append([4,5])
print(lista)

print("""
 clear
 utilizamos o clear para limpar a lista
""")
print(lista)
lista.clear()
print(lista)

print("""
 copy
 utilizamos o copy para copiar a lista em outra instancia
""")
lista.append(1)
print(id(lista))
# se atribuimos a variavel l2 uma lista elas tem a mesma instancia 
l2 = lista
print(id(l2))
l2.append(2)
print(lista)
print(l2)
# utilizando o copy podemos alterar l2 e isso nao reflete na lista
l2 = lista.copy()
print(id(l2))
l2.append(3)
print(f"l2 = {l2}")
print(f"lista = {lista}")

# utilizando o count para contar quantas vezes um objeto aparece na lista
cores = ["azul", "preto","azul", "preto"]
contagemAzul = cores.count("azul")
print(f" O azul aparece {contagemAzul} vezes na lista")

# utilizando o extend para adicionar varios elementos dentro da lista
listaNomes = ["joao","pedro"]
listaNomes.extend(["leo","joao"])
print(listaNomes)

# utilizando o indice recumeramos a posicao da primeira ocorrencia do elemento

print(listaNomes.index("joao"))

# por padrao oma lista em python funciona com uma estrutura de dados(pilha)
# entao quando utilizamos o pop retiramos o ultimo elemento da lista

listaNomes.pop()
listaNomes.pop()
print(listaNomes)# joao , pedro

# mais tambem podemos passar o indice e escolher qual elemento queremos remover
listaNomes.pop(0) # remove joao
print(listaNomes) # pedro

# utilizamos o remove para remover um objeto da lista
listaNomes.append("leo") 
print(listaNomes)# pedro, leo
listaNomes.remove("pedro")
print(listaNomes) # leo


print("utilizamos o reverse para inverter a lista")
numeros = [0,1,2]
print(numeros)
numeros.reverse()
print(numeros) # 2,1,0

print(" com o sort ordenamos alfabeticamente uma lista")
letras = ["b","c","a"]
letras.sort()
print(letras)

numeros = [2,3,1]
numeros.sort()
print(numeros)

print(" com o len descobrimos o tanhado o objeto ou a quantidade de elementos de uma lista")
print(len(numeros))# len e uma funcao por isso passamos como argumento o elemento que queremos medir o tamanho


print(" sorted é uma funcao passamos para ele o elemento ou lista que queremos ordenar alfabeticamente ")
nome = "joao"
print(sorted(nome))


