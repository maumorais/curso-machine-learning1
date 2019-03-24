import pandas as pd

df = pd.read_csv('../download/busca.csv')
X_df = pd.get_dummies(df[['home','busca','logado']])
Y_df = df['comprou']
X = X_df.values
Y = Y_df.values

porcentagem_de_treino = 0.8
porcentagem_de_teste = 0.1
tamanho_de_treino = int(porcentagem_de_treino * len(Y))
tamanho_de_teste = int(porcentagem_de_teste * len(Y))
tamanho_de_validacao = len(Y) - (tamanho_de_treino + tamanho_de_teste)

treino_dados = X[:tamanho_de_treino]
treino_marcacoes = Y[:tamanho_de_treino]
teste_dados = X[tamanho_de_treino:tamanho_de_teste+tamanho_de_treino]
teste_marcacoes = Y[tamanho_de_treino:tamanho_de_teste+tamanho_de_treino]
validacao_dados = X[-tamanho_de_validacao:]
validacao_marcacoes = Y[-tamanho_de_validacao:]

def calcula_acerto(resultado, marcacoes, dados):
    acertos = resultado == marcacoes

    total_de_acertos = sum(acertos)

    taxa_de_acerto = 100.0 * total_de_acertos / len(dados)
    return taxa_de_acerto

def fit_and_predict(modelo, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes):
    modelo.fit(treino_dados, treino_marcacoes)

    resultado = modelo.predict(teste_dados)
    return calcula_acerto(resultado, teste_marcacoes, teste_dados)



from sklearn.naive_bayes import MultinomialNB
modeloNB = MultinomialNB()
taxa_acerto_NB = fit_and_predict(modeloNB, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes)
print("Taxa de acerto do MultinomialNB: {0}".format(taxa_acerto_NB))

from sklearn.ensemble import AdaBoostClassifier
modeloAda = AdaBoostClassifier()
taxa_acerto_Ada = fit_and_predict(modeloAda, treino_dados, treino_marcacoes, teste_dados, teste_marcacoes)
print("Taxa de acerto do AdaBoostClassifier: {0}".format(taxa_acerto_Ada))

if(taxa_acerto_NB > taxa_acerto_Ada):
    vencedor = modeloNB
else:
    vencedor = modeloAda

resulado_vencedor = vencedor.predict(validacao_dados)
taxa_acerto_vencedor = calcula_acerto(resulado_vencedor, validacao_marcacoes, validacao_dados)
print("Taxa de acerto do Vencedor entre os dois algoritmos no mundo real: {0}".format(taxa_acerto_vencedor))

total_de_elementos = len(teste_dados)

from collections import Counter
acerto_base = max(Counter(validacao_marcacoes).values())
taxa_de_acerto_base = 100.0 * acerto_base / len(validacao_marcacoes)

print('Taxa de acerto base: %f' % taxa_de_acerto_base)
print('Total de elementos: %d' % total_de_elementos)