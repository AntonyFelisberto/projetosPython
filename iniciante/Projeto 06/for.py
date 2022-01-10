def loopForComNumeros():
    for x in range(0,10):#vai de 0 até 9
        print(x)
    print("\n")
    for i in range(1,11):#vai de 1 até 10,sempre que no for incremente mais um numero se usar o numero 1
        print(i)

def loopForComArrays():
    dias={"segunda","terça","quarta","quinta","sexta","sabado","domingo"}#somente strings
    numero={"idade":19,"casa":130,"preço":1500.00}#nome da varivel:valor
    for i in dias:
        print(i)#imprime os valores de strings
    print("\n")
    for x in numero:
        print(x)#imprime os valores de strings
        print(numero[x])#imprime os valores armazenados em cada string

def loopForComVariantes(variante):
    for i in variante:
        print("a posição é {}".format(i))

def loopEnumerandoPosicoes():
    dias = {"segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo"}
    for variavelDePosicao,variavelDeValor in enumerate(dias):#o enumerate() passa as posições de cada item no array para a variavel de posição
        print(variavelDePosicao,variavelDeValor)
loopForComArrays()
loopForComNumeros()
contagem=int(input("digite o numero para utilizar no for"))
loopForComVariantes(contagem)
loopEnumerandoPosicoes()