global r

def numeroSomar(variavel):
    resp = str(input("após isso deseja decrementar o numero ?"))

    while variavel < r:
        print("o numero esta em loop na posição {}".format(variavel + 1))
        variavel = variavel + 1

    if resp.count("s")!=0:          #o count verifica se a pessoa digitou s ou a string que você quiser e o != 0 é porque o count retorna 1(verdadeiro) ou 0(falso)
        print("good choise")
        return 0
        pass
    else:
        print("ok")
        return 1
        pass


def numeroSubtrair(variavel):
    variavel=r
    while variavel>0:
        print("o numero esta em loop na posição {}".format(variavel))
        variavel = variavel - 1

i = int(0)
r = int(input("digite quantas vezes os itens vão ficar em loop:"))
if(numeroSomar(i)==0):
    numeroSubtrair(i)
    pass