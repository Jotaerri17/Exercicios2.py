

# 3-Positivo ou Negativo

#num=int(input("Digite um número: ")) #Requisição do numero
#if num > 0:                          #Validações para o num
#    print("O número é positivo 👌")
#elif num < 0:
#    print("O numero é negativo ✌️")
#elif num == 0:
#    print("O numero é neutro 👍")





# 11-Cadastro de Funcionários


#def cadastrar_funcionarios(): #Função referente ao cadrasto
#    funcionarios = [] #Local onde serão armazenado os dados dos funcionarios
#    while True: #Loop
#        nome = input("Digite seu nome: ")
#        idade = input("Digite sua idade: ")
#        cargo = input("Digite seu cargo: ") #Requisição dos dados

#        funcionario = {"nome": nome, "idade": idade, "cargo": cargo} #Definição de cada variavel
#        funcionarios.append(funcionario) #Adiciona o funcionario a lista

#        alternativa = input("Quer cadastrar mais um funcionarios? [S/N]: ").upper() # Escolha de adicionar outro funcionario
#        if alternativa == "N":
#            break #Caso digite "N" ele para o loop

#    print("\nFuncionários cadastrados:")
#    for i, l in enumerate(funcionarios, start=1): #Enumera os funcionarios, começando em 1
#        print(f"{i}. Nome: {l['nome']}, Idade: {l['idade']}, Cargo: {l['cargo']}") #Mostra os Dados do funcionario



#cadastrar_funcionarios() #Retorna a função



# 25-Validação de cpf

#cpf = str(input("Digite seu CPF:")) #Requisição do CPF

#cpf= cpf.replace(".","").replace("-","") #Substitui os "." e "-" por vazio

#if not cpf.isnumeric(): #Verifica se a variavel cpf contem apenas numeros
#    print("CPF invalido!")
#elif len(cpf) == 11: #Verifica se a variavel cpf possui 11 numeros
#    print("CPF valido!")
#
# primeira_parte = cpf[0:3] #Separa os 11 digitos do cpf em 4 partes para depois organiza-los
# segunda_parte = cpf[3:6]
# terceira_parte = cpf[6:9]
# quarta_parte = cpf[9:11]
# print(f"{primeira_parte}.{segunda_parte}.{terceira_parte}-{quarta_parte}")






# import sympy as sp
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Definindo a variável simbólica
# t = sp.symbols('t')
#
# # Função da posição x(t)
# x = 4 - 27*t + t**3
#
# # Derivando para obter a velocidade v(t) e aceleração a(t)
# v = sp.diff(x, t)
# a = sp.diff(v, t)
#
# print("Função posição: x(t) =", x)
# print("Função velocidade: v(t) =", v)
# print("Função aceleração: a(t) =", a)
#
# # Convertendo para funções numéricas para plot
# x_func = sp.lambdify(t, x, modules='numpy')
# v_func = sp.lambdify(t, v, modules='numpy')
# a_func = sp.lambdify(t, a, modules='numpy')
#
# # Criando o intervalo de tempo de 0 a 5 segundos
# tempo = np.linspace(0, 5, 200)
#
# # Plotando os gráficos
# plt.figure(figsize=(10, 6))
# plt.plot(tempo, x_func(tempo), label='x(t) - posição', color='blue')
# plt.plot(tempo, v_func(tempo), label='v(t) - velocidade', color='green')
# plt.plot(tempo, a_func(tempo), label='a(t) - aceleração', color='red')
# plt.xlabel('Tempo (s)')
# plt.ylabel('Funções')
# plt.title('Análise de Movimento de uma Partícula')
# plt.legend()
# plt.grid(True)
# plt.show()
#
# # Problema 2 - Encontrar quando a velocidade é zero
# t_zero = sp.solve(v, t)
# print("\nInstante(s) em que a velocidade é zero:")
# for sol in t_zero:
#     if sol > 0:
#         print(f"t = {sol} s (a partícula está momentaneamente em repouso)")
#
# # Extra: Destacar o(s) ponto(s) onde v(t) = 0
# plt.figure(figsize=(8, 5))
# plt.plot(tempo, v_func(tempo), label='v(t)', color='green')
# for sol in t_zero:
#     if sol >= 0:
#         plt.scatter(float(sol), 0, color='red', zorder=5, label=f'v=0 em t={sol}')
# plt.title('Velocidade v(t) e ponto de repouso')
# plt.xlabel('Tempo (s)')
# plt.ylabel('Velocidade')
# plt.axhline(0, color='black', linewidth=0.5)
# plt.legend()
# plt.grid(True)
# plt.show()

# Usa o sympy para calcular as derivadas de posição → velocidade → aceleração.
# Plota as três funções em um gráfico.
# Resolve a equação v(t) = 0
# Exibe os instantes em que a partícula para.
# (Extra) Destaca no gráfico da velocidade o ponto onde ela zera.




import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Dados da Tabela
modelo_a = [89.49,87.59,89.94,92.57,87.30,87.30,92.74,90.30,86.59,89.63,
            86.61,86.60,88.73,82.26,82.83,86.31,84.96,88.94,85.28,83.76]
modelo_b = [77.92,82.90,83.29,80.99,84.19,87.02,94.43,85.87,86.29,84.63,
            75.41,84.87,85.30,97.32,84.04,86.51,84.83,79.16,90.71,88.76]
modelo_c = [90.72,91.12,92.17,92.11,87.24,88.12,91.03,91.03,91.03,97.71,
            91.14,92.27,91.91,91.30,89.37,91.52,88.45,89.53,89.03,90.16]

# Função para estatísticas
def estatisticas(modelo):
    media = np.mean(modelo)
    mediana = np.median(modelo)
    variancia = np.var(modelo, ddof=1)
    desvio_padrao = np.std(modelo, ddof=1)
    return media, mediana, variancia, desvio_padrao

# Cálculo para cada modelo
ma, mda, vara, sdpa = estatisticas(modelo_a)
mb, mdb, varb, sdpb = estatisticas(modelo_b)
mc, mdc, varc, sdpc = estatisticas(modelo_c)

# Exibição dos resultados
print("Modelo A - Média:", round(ma,2), "Mediana:", mda, "Variância:", round(vara,2), "Desvio Padrão:", round(sdpa,2))
print("Modelo B - Média:", round(mb,2), "Mediana:", mdb, "Variância:", round(varb,2), "Desvio Padrão:", round(sdpb,2))
print("Modelo C - Média:", round(mc,2), "Mediana:", mdc, "Variância:", round(varc,2), "Desvio Padrão:", round(sdpc,2))

# Verificação de consistência (menor desvio padrão)
desvios = {"A": sdpa, "B": sdpb, "C": sdpc}
modelo_consistente = min(desvios, key=desvios.get)
print(f"\nModelo mais consistente: Modelo {modelo_consistente} (Menor desvio padrão: {desvios[modelo_consistente]:.2f})")

# Gráfico boxplot
plt.figure(figsize=(10, 6))
plt.boxplot([modelo_a, modelo_b, modelo_c], labels=['Modelo A', 'Modelo B', 'Modelo C'])
plt.title("Boxplot dos Modelos")
plt.ylabel("Percentual de Acerto")
plt.grid(True)
plt.show()

# Gráfico de Histograma
plt.figure(figsize=(10, 6))
plt.hist(modelo_a, bins=10, alpha=0.5, label='Modelo A')
plt.hist(modelo_b, bins=10, alpha=0.5, label='Modelo B')
plt.hist(modelo_c, bins=10, alpha=0.5, label='Modelo C')
plt.title("Histograma dos Modelos")
plt.xlabel("Percentual de Acerto")
plt.ylabel("Frequência")
plt.legend()
plt.grid(True)
plt.show()

# SymPy - Média simbólica e derivada
a, b, c = sp.symbols('a b c')
media_simbolica = (a + b + c) / 3
derivada_b = sp.diff(media_simbolica, b)

print("\nMédia simbólica:", media_simbolica)
print("Derivada da média em relação a b:", derivada_b)

