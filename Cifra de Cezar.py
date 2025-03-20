#Cifra de Cezar
frase=str(input("Digite uma frase:")).lower()
num=int(input("Digite um numero para ser usado como chave:"))
alfabeto="abcdefghijklmnopqrstuvwxyz"

def cifrar(frase,num):
    resultado = ""
    for letra in frase:
        if letra in alfabeto:
            posicao = alfabeto.index(letra)
            nova_posicao = (posicao + num) % len(alfabeto)
            resultado += alfabeto[nova_posicao]
        else:
            # Se não é uma letra (espaço, números, pontuação), adiciona diretamente
            resultado += letra
    return resultado


def decifrar(frase, num):
    resultado = ""
    for letra in frase:
        if letra in alfabeto:
            posicao = alfabeto.index(letra)
            nova_posicao = (posicao - num) % len(alfabeto)
            resultado += alfabeto[nova_posicao]
        else:
            # Se não é uma letra (espaço, números, pontuação), adiciona diretamente
            resultado += letra
    return resultado


cifrado = cifrar(frase, num)
print(f"Frase cifrada: {cifrado}")

decifrado = decifrar(cifrado, num)
print(f"Frase decifrada: {decifrado}")