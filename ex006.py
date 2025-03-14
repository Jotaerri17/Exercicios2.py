#import random

#low=0
#rigth=500
#ptions=("pedra","papel","tesoura")
#cards=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]


#number=random.random
#number=random.randint(low, rigth)
#escolha=random.choice(options) #Escolher algo aleatorios dentro da variavel
#print(number)
#print(escolha)
#random.shuffle(cards) #muda a ordem da variavel aleatoriamente
#print(cards)



#Jogo da Adivinhação
import random
pc=random.randint(0,20)
while True:
    escolha=int(input("Digite um numero de 0 a 20:" ))
    if escolha==pc:
        print("Parabéns vc acertou!")
        break
    else:
        print("Você errou!")
        if escolha>pc:
            print("O numero é menor")
        elif escolha<pc:
            print("O numero é maior")
    cont=str(input("Deseja continuar? [S/N]:")).upper()
    if cont=="S":
        continue
    else:
        print(f" O numero era {pc}")
        print("Obrigado por jogar!")
        break


























