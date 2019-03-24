import csv

def carregar_buscas():
    X = []
    Y = []

    arquivo = open('../download/busca.csv','r')
    leitor = csv.reader(arquivo)
    next(leitor)

    for home, busca, logado, comprou in leitor:
        elemento = [int(home), busca, int(logado)]
        X.append(elemento)
        Y.append(int(comprou))
    
    """ Debug info 
    print(X)
    print(len(X))
    print(Y)
    print(len(Y))
    """

    return X, Y
 