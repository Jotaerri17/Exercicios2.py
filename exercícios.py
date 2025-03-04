#print('hello world')

#num= (int(input('Digite um numero: ')),
   #   int(input('Digite um numero: ')),
    #  int(input('Digite um numero: ')),
     # int(input('Digite um numero: ')))
#print(f'Voçe digitou os valores {num}')
#if 9 in num:
 #   print(f'O valor 9 apareceu {num.count(9)} vezes')
#else:
 #   print('O numero 9 nao foi encontrado')
#if 3 in num:
 #   print(f'O numero 3 apareceu na posição {num.index(3)+1}')
#else:
 #   print('O valor 3 nao foi encontrado')
#for n in num:
 #   if n%2==0:
  #      print(f'O numero {n} é par')

#lista
#valores=[]
#for cont in range (1,5):
 #   valores.append(int(input('Digite um valor: ')))
#a1= valores.index(max(valores))
#b1= valores.index(min(valores))
#print(valores)
#print(f'O maior valor foi {max(valores)} na posição {a1}')
#print(f'O menor valor foi {min(valores)} na posição {b1}')


#numeros=[]
#while True:
#    num =int(input('Digite um numero: '))
#    if num in numeros:
#        print('O numero ja existe na lista! Não sera adicionado')
#    else:
#        numeros.append(num)
#        print('Valor adicionado com sucesso')
#    c=str(input('Quer continuar? [S/N]')).upper()
#    if c=='N':
#   print(f'Os numeros digitados foram {numeros}')
#    break
#print('Programa finalizado')

#list=[]
#for c in range(0,5):
#    num=int(input('Digite um numero:'))
#    if c==0 or num>list[-1]:
#        list.append(num)
#    else:
#        pos=0
#        while pos<len(list):
#            if num<=list[pos]:
#               list.insert(pos,num)
#               break
#            pos+=1
#print('-=' *30)
#print(f'Os valores digitados em ordem foram {list}')


#numeros=[]
#cont=0
#while True:
#    num =int(input('Digite um numero: '))
#    numeros.append(num)
#    cont+=1
#    print('Valor adicionado com sucesso')
#    c=str(input('Quer continuar? [S/N]')).upper()
#    if c=='S':
#        continue
#    if c=='N':
#        numeros.sort(reverse=True)
#        print(f'Os numeros digitados foram {numeros}')
#        print('-=' *30)
#        print(f'O numero de elementos foi {cont}')
#        if cont in numeros:
#            print(f'O numero {cont} apareceu na posição {numeros.index(cont)+1} da lista')
#        else:
#            print(f'O numero {cont} nao foi encontrado')
#    print(f'Os numeros pares digitados foram', [num for num in numeros if num%2==0])
#    print(f'Os numeros impares digitados foram', [num for num in numeros if num%2!=0])
#    print('-=' *30)
#    print('Programa finalizado')
#   break



#exp=str(input('Digite sua expressão:'))
#if exp.count('(')==exp.count(')'):
#    print('Sua expressão é valida!')
#else:
#    print('Sua expressão esta invalida.. Tente novamente!')