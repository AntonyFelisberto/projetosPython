import urllib.request #necessario para se conectar ao link

def conectarInternet():
    objUrl=urllib.request.urlopen("http://www.google.com") #urlopen -com qual conteudo vai se conectar

    if objUrl.getcode()==200:#getcode retorna o código http se a conexão foi efetuada com sucesso
        dados=objUrl.read()
        print(dados)

conectarInternet()