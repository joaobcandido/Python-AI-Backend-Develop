# a estrutura condicional permite o desvio do fluxo de controle,
# quando determinadas expressões lógicas são atendidas.
saldo = 2000.0
saque = float(input("informe o valor do saque : "))

if saldo >= saque :
    print("realizando o saque, aguarde ........")

else :
    print("Saldo insuficiente")

##################################################################
opcao = int(input("Informe uma opcao:\n[1] sacar \n[2] extrato \nopcao: "))
if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
elif opcao == 2:
    print("Exibindo o extrato....")
else:
    print("Opcao invalida")

##############################################################
# if ternario 
saldo = 100
saque = 50
status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!!!")