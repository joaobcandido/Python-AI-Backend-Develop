# o que são operadores logicos?
# são operadores utilizados em conjunto
#  com operadores de comparação para montar uma expressão logica

print(True and True and True)
print(True and True and False)
print(True or False or False)

saldo = 100
saque = 230

# OR = para ser true apenas um tem que ser true
exp = saldo > saque or saldo < saque
print("expressao logica = ",exp)

# AND = para ser true tudo tem que ser true
exp = saldo > saque and saldo < saque
print("expressao logica = ",exp)