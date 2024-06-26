nome = "Joao Batista Candido"
# acessando pelo indice
print(nome[0])
# acessando sem passar o start(inicio)
print(nome[:6])
# acessando sem passar o stop(fim)
print(nome[5:])
# acessando um sub string
print(nome[5:13])
# acessando um sub string e definindo um step(passo)
# obs: se passar step 1 retorna a string original
print(nome[5:13:2])
# espelhando a string passando step -1
print(nome[::-1])
