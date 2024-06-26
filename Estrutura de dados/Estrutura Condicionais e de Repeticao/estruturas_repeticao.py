# as estruturas de repeticao são utilizadas para repetir um trecho de codigo por um determinado
#numeros de vezes.

texto = input("informe um texto :")
VOGAIS = "AEIOU"

#comando for repete o bloco de codigo por  quantas vezes estiver definida na interacao
for letra in texto:
    # transformando letra em maiusculo
    if letra.upper() in VOGAIS: 
        # por default o print tem uma quebra de linha, colocando (end=" ") exibimos tudo na mesma linha 
        print(letra,end=" ")

print()

################################################################

#funcao range com dois argumentos(inicio,fim-1)
for numero in range(0,19):
    print(numero, end=" ")

print()

#funcao range com tres argumentos(inicio,fim-1,step)
for numero in range(0,51,5):
    print(numero, end=" ")

print()
# comando while repete o bloco de codigo varias vezes
numero = 3
while numero < 4:
    print(numero)
    numero +=1
    
