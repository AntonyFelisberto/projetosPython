valor=input("Digite algo:")
print("o tipo do valor digitado é {}".format(type(valor)))#type mostra qual tipo primitivo é o valor
print("o tipo do valor digitado é {}".format(valor.isspace()))#isspace verifica se só tem espaços
print("o valor é numerico ?:{}".format(valor.isnumeric()))#isnumeric verifica se o valor digitado é um numero
print("o valor é alfabetico ?:{}".format(valor.isalpha()))#isalpha verifica se o valor digitado é alfabetico
print("o valor é alfanumérico ?:{}".format(valor.isalnum()))#isalnum verifica se o valor digitado é alfanumerico
print("substituindo valores:{}".format(valor.replace("a","o")))#replace("antiga","nova") substitui os caracteres por outro
print("o valor esta minusculo ?:{}".format(valor.islower()))#islower() verifica se o valor esta em minusculo
print("o valor esta maiusculo ?:{}".format(valor.isupper()))#isupper verifica se o valor esta em maiusculo
print("o valor esta capitalizado ?:{}".format(valor.istitle()))#istitle verifica se tem letras minusculas e maiusculas