

# 3-Positivo ou Negativo

num=str(input("Digite um número: ")) #Requisição do numero
if num > 0:                          #Validações para o num
    print("O número é positivo 👌")
elif num < 0:
    print("O numero é negativo ✌️")
elif num == 0:
    print("O numero é neutro 👍")





# 11-Cadastro de Funcionários


def cadastrar_funcionarios(): #Função referente ao cadrasto
    funcionarios = [] #Local onde serão armazenado os dados dos funcionarios
    while True: #Loop
        nome = input("Digite seu nome: ")
        idade = input("Digite sua idade: ")
        cargo = input("Digite seu cargo: ") #Requisição dos dados#

        funcionario = {"nome": nome, "idade": idade, "cargo": cargo} #Definição de cada variavel
        funcionarios.append(funcionario) #Adiciona o funcionario a lista

        alternativa = input("Quer cadastrar mais um funcionarios? [S/N]: ").upper() # Escolha de adicionar outro funcionario
        if alternativa == "N":
            break #Caso digite "N" ele para

    print("\nFuncionários cadastrados:")
    for i, l in enumerate(funcionarios, start=1): #Enumera os funcionarios, começando em 1
        print(f"{i}. Nome: {l['nome']}, Idade: {l['idade']}, Cargo: {l['cargo']}") #Mostra o Dado do funcionario



cadastrar_funcionarios() #Retorna a função



# 25-Validação de cpf

cpf = str(input("Digite seu CPF:")) #Requisição do CPF

cpf= cpf.replace(".","").replace("-","") #Substitui os "." e "-" por vazio

if not cpf.isnumeric(): #Verifica se a variavel cpf contem apenas numeros
    print("CPF invalido!")
elif len(cpf) == 11: #Verifica se a variavel cpf possui 11 numeros
    print("CPF valido!")

primeira_parte = cpf[0:3] #Separa os 11 digitos do cpf em 4 partes para depois organiza-los
segunda_parte = cpf[3:6]
terceira_parte = cpf[6:9]
quarta_parte = cpf[9:11]
print(f"{primeira_parte}.{segunda_parte}.{terceira_parte}-{quarta_parte}")









