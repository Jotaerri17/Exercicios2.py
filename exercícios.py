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
valores=[]
for cont in range (1,5):
    valores.append(int(input('Digite um valor: ')))
a1= valores.index(max(valores))
b1= valores.index(min(valores))
print(valores)
print(f'O maior valor foi {max(valores)} na posição {a1}')
print(f'O menor valor foi {min(valores)} na posição {b1}')



