aluno = {}

def notas(*n, sit=False):

    '''
    --> Função para analizar notas e situções de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opicional, indicando se deve ou não adicionar a situação
    :return: dicinário cim várias informações sobre a situação da turma.
    '''

    aluno['total'] = len(n)
    aluno['maior'] = max(n)
    aluno['menor'] = min(n)
    aluno['media'] = sum(n) / len(n)

    if sit == True:
        if aluno['media'] >= 7:
            aluno['situação'] = 'BOA !'

        elif 5 <= aluno['media'] < 7:
            aluno['situação'] = 'RAZOÁVEL !'

        else:
            aluno['situação'] = 'RUIM !'

    return (aluno)


resp = notas(6.8, 5.2, 4.5, sit=True)
print(resp)