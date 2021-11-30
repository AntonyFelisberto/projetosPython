class minhaClasse():#() ->caso essa classe fosse herdar de outra você colocaria o nome dela dentro do parentes (nomeClasse)
    def __init__(self):#esse __init__(self) seria como um método contrutor do java
        self.meuAtributo="passou pelo construtor"#self seria para criar variaveis da classe e poder acessalas

    def primeiroMetodo(self):
        print("passou pelo metodo")

    def segundoMetodo(self,valor):
        self.outroAtributo=valor
        print(self.outroAtributo)

def instanciandoObjetoDoTipoClasse():
    objeto=minhaClasse()#instanciando classe em python
    var=objeto.meuAtributo
    print(var)
    objeto.primeiroMetodo()
    objeto.segundoMetodo(19)

instanciandoObjetoDoTipoClasse()