def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de varios alunos.
    :param n: uma ou mais notas
    :param sit: valor opcional, indicando se deve ou nao adicionar a situação.
    :return: dicionario com varias informações sobre a stirução da turma.
    """

    r=dict()
    r['total']=len(n)
    r["maior"]=max(n)
    r["menor"]=min(n)
    r["media"] = round(sum(n) / len(n), 1)
    if sit:
        if r["media"]>=7:
            r["situacao"]="BOA"
        elif r["media"]>=5:
             r["situação"]= "Razoável"
        else:
            r["situacao"] = "RUIM"


    return r

#Progama principal
resp= notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
#help(notas)