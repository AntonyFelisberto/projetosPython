# em python você não precisa dizer qual o tipo da variavel ao criala

nome = "antony"
idade = 19
peso = 50

# tipos de print na tela
# só string
print("ola")
# contas
print(7 + 1)
# concatenação
print("7" + "1")
# print("ola"+5) não é possivel concatenar numeros com o +
# concatenação de numero e string
print("ola", 5)
# concatenação de variaveis
print(nome, peso, idade)
# print(nome + peso + idade) não é possivel concatenar numeros com o +

# fazer variaveis receber valores e dizer qual o tipo desse valor:  tipo(input("o que aparece na tela))
nomeUsuario = str(input("qual seu nome:"))
idadeUsuario = int(input("qual sua idade:"))
pesoUsuario = float(input("qual seu peso:"))

print("seu nome é :", nomeUsuario, "sua idade é :", idadeUsuario, "seu peso é :", pesoUsuario)

numeroParaSoma = int(input("digite um  numero para soma:"))
numeroParaSomar = int(input("digite um segundo numero para soma:"))
numerosSomados = numeroParaSomar + numeroParaSoma
print("a soma dos dois numeros foi :", numerosSomados)

valor = str(input("digite algo para aparecer na tela"))
print("o valor digitado foi: {}".format(valor)) # as {} servem pra dizer que um valor vai ser inserido la dentro usando o .format(valorQueVaiSerInserido,valorQueVaiSerInserido....)


