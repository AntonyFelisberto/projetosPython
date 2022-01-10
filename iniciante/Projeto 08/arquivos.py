def escreverArquivo():
    arquivo = open("novoArquivo.txt",
                   "r+")  # nomevariavel = (nome,w+ cria um arquivo para leitura e escrita r+ arquivo para leitura e escrita,r só leitura)
    arquivo.write("escrevendo no arquivo\r\n")  # write escreve no arquivo  e  \n pula linha
    arquivo.close()  # fechar arquivo


def escreverArquivoP():
    arquivo = open("novoArquivo.txt","a+")  # nomevariavel = (nome,w+ cria um arquivo para leitura e escrita a+ escrever nas proximas linhas do arquivo)
    arquivo.write("escrevendo no arquivo\r\n")  # write escreve no arquivo  e  \n pula linha
    arquivo.close()  # fechar arquivo


def lerArquivo():
    arquivo = open("novoArquivo.txt", "r")
    if arquivo.mode == "r":  # .mode==r só vai executar o arquivo se estiver em modo de leitura
        conteudo = arquivo.read()  # variavel recebe conteudo do arquivo, read() faz a leitura de todo o arquivo
        print(conteudo)
        arquivo.close()
        pass


def lerArquivosGrandes():
    arquivo = open("novoArquivo.txt", "r")
    if arquivo.mode == "r":  # .mode==r só vai executar o arquivo se estiver em modo de leitura
        conteudo = arquivo.readlines()  # readlines() vai ler todas as linhas do arquivo
        for conteudoTotal in conteudo:  # enquanto o conteudoTotal não chegar até o final do conteudo ele vai ficar em loop
            print(conteudoTotal)
        arquivo.close()
        pass


escreverArquivo()
escreverArquivoP()
lerArquivo()
lerArquivosGrandes()
