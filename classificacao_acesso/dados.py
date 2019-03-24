import csv

def carregar_acessos():
    X = []
    Y = []

    arquivo = open('../download/acesso.csv','r')
    leitor = csv.reader(arquivo)
    next(leitor)

    for home, como_funciona, contato, comprou in leitor:
        X.append([int(home), int(como_funciona), int(contato)])
        Y.append(int(comprou))
    
    """ Debug info 
    print(X)
    print(len(X))
    print(Y)
    print(len(Y))
    """

    return X, Y