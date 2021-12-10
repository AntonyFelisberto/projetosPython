import numpy

#usando array com numpy
#ao inicializar o array com um valor os outros tambem tem que ser desse valor ex("string","string"...)(int,int,int....)
#o numpy te oferece algumas opçoes a mais do que o array convencional
listagem=numpy.array(["valor","valores","validades"])
listar=["valor","valores","validades"]
                #lista convencional
#nomeLista * numero        repeta a lista o numero de vezes que voce colocou
#"caracter" * numero       repete o numero de vezes que você colocou
                #numpy
#os elementos vão se comportar mais como um vetor 
#nomeLista * numero         se a lista for numerica ela vai multiplica todos os valores pelo numero que você colocar
#                           você tambem pode fazer outras contas como +,-,/,%....
#nomeLista * nomeLista      multiplica a lista dos numeros na mesma posição ex:i[1] i[1]==1 i[1,4] i[1,4]==i[1,16]      você tambem pode fazer outras contas como +,-,/,%....

                #matrizes tem que ser numpy.array
#matriz=[[1,5],[30,100]]

#print(matriz[1,0])
            #vai exibir 30,   1 posição matriz 0 coluna

matriz=numpy.array([[1,5],[30,100]])

print(matriz[1,0])
            #vai exibir 30,   1 posição matriz 0 coluna

#cubos,cubos tem 3 dimensões mas se você quiser você pode criar quantas dimensões quiser
cubo=numpy.array([[[50,10],[50,20]],[[6,7],[80,101]]])

print(cubo.shape) #vai trazer quantas dimensões o array tem

print(cubo[1,1,0])#exibe o valor 80,sempre comece da posição 0


#fazendo a lista com qualquer valor possivel
listas=["valor","valores","meu valor",1.5,1,True,False,["outra lista dentro da lista",1,2.7,False]]

#fazendo listas de tuplas
listasTuplas=[(0,"nas tuplas os elementos não podem ser alterados"),(1,"nas tuplas são usados () e você pode inserir o que quiser igual a lista")]

#lista comum
lista=["ola","quem","é","voce"]

#listas com range enumerado
for numeroDaPosicao,lista in enumerate(lista):
    print(numeroDaPosicao,lista)

#percorrendo a lista com foreach
for percorrerLista in listas:
    print(listas)

#percorrendo a lista com range
for i in range(0,9):
   print(listas)

#o python sempre começa a percorrer pelo 0 ou seja a lista sempre vai começar em 0
print(listas[5])
print(listas[7][0])
print(range(6))
print(list(range(6)))

#percorrendo a lista com o range definido
for i in range(6):
    print(listas)

