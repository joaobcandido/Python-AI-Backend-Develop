nome = "Joao"
idade = 46
# utilizando  um dicionario
dados = {"nome": "joao","idade": 46}
# formatacao com %
print("Olá, me chamo %s.\nEu tenho %d de idade."%(nome,idade))
# formatacao com o metodo format
print("Olá, me chamo {0}.\nEu tenho {1} de idade.".format(nome,idade))
# formatacao com metodo format passando como argumento um dicionario
print("Olá, me chamo {nome}.\nEu tenho {idade} de idade.".format(**dados))
# metodo f-string
print(f"Olá, me chamo {nome}.\nEu tenho {idade} de idade.")