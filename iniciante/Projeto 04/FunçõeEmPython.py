global variavel #variavel global que pode ser acessada em qualquer função ou local
variavel=1

def funcaoSemRetorno():
    print("ola funcao sem retorno")

def funcaoComRetornoERecebimento(s):#variavel que armazena valores recebidos
    print(s)
    print(variavel)
    print("ola funcao com retorno")
    return 23   #valor que retorna podendo ser contas,variaveis ou valores

s=int(input("digite um numero"))
funcaoSemRetorno()
print(funcaoComRetornoERecebimento(s))#pode passar como parametro variaveis ou valores
m=int(funcaoComRetornoERecebimento(s))
print(m+15)
print(variavel)