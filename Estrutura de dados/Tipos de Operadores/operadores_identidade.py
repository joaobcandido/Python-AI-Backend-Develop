# o que são os operadores de identidade?
# são operadores usados para comparam se dois objetos testados ocupam a mesma posição na memória.
saldo = 200
limite = 230
# nesse caso a resposta e False
print(saldo is limite)

saldo = 2000
limite = 2000
# nesse caso a resposta e True
print(saldo is limite)