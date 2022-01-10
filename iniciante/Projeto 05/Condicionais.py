def verificarMaior(x,y):
    if(x<y):
        print("x é menor que y")
        pass
    elif(x>y):
        print("x é maior que y")
        pass
    else:
        print("x e y são iguais")
        pass


x=int(input("digite um numero:"))
y=int(input("digite outro numero:"))
verificarMaior(x,y)