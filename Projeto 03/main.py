# cores no terminal sempre começam com \033[m entre o colchete e o m você vai colocar o código
# \033[ |     |      |  m   exemplo \033[0;33;44m
#     style;text;back
# style:0-none,1-negrito,4-sublinhado,7-troca o text e o back
# text:30-branco,31-vermelho,32-verde,33-amarelo,34-azul,35-roxo,36-ciano,37-cinza,pra usar mais é preciso usar bibliotecas
# back:40-branco,41-vermelho,42-verde,43-amarelo,44-azul,45-roxo,46-ciano,47-cinza,pra usar mais é preciso usar bibliotecas
print("\033[0;33;40mOLA MUNDO")
print("ola")


cores={"nome":"\033[m",
       "azul":"\033[34m",
       "amarelo":"\033[33m",
       "pretoEBranco":"\033[7;30m"}#criando um array com as cores pré estabelecidas

print("{}{}{}usando cores ja pré estabelecidas em array".format(cores["pretoEBranco"],cores["azul"],cores["amarelo"]))

corDoTexto = int(input("digite 0-none,1-negrito,4-sublinhado,7-troca"))
corDaLetra = int(input("digite um numero de 30 a 37"))
corDeFundo=int(input("digite um numer de 40 a 47"))


while corDoTexto<0 or (corDaLetra<30 or corDaLetra>37) or (corDeFundo<40 or corDeFundo>47):
    corDoTexto=int(input("digite 0-none,1-negrito,4-sublinhado,7-troca"))
    corDaLetra=int(input("digite um numero de 30 a 37"))
    corDeFundo = int(input("digite um numer de 40 a 47"))

print("\033[{};{};{}m olaaaaa".format(corDoTexto,corDaLetra,corDeFundo))

