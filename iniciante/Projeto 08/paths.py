from os import path     #é assim que se faz importação de bibiliotecas em python
import time

def dadosArquivo():
    arquivoExiste=path.exists("novoArquivo.txt") #exists verifica se o arquivo existe
    diretorio = path.isdir("novoArquivo.txt")   #isdir pega o local do arquivo
    pathArquivo=path.realpath("novoArquivo.txt") #realpath pega o caminho até o arquivo
    pathRelativo= path.realpath("novoArquivo.txt") #realpath pega o caminho relativo do arquivo
    dataCriacao= time.ctime(path.getctime("novoArquivo.txt"))
    dataModificacao= time.ctime(path.getmtime)

    print(arquivoExiste)
    print(diretorio)
    print(pathArquivo)
    print(pathRelativo)
    print(dataCriacao)
    print(dataModificacao)