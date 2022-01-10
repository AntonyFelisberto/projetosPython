import pymongo
from pymongo import MongoClient

def manipularDadosDoMongo():
    cliente=pymongo.MongoClient("mongodb://localhost:3306")
    db=cliente.ComoVaiSerChamadoADatabase

    for i in range (1,10):      #vai incrementar até chegar a 10
        objDic= {"codigo":i}    #cria um array e faz código receber posição i
        db.conhecer.insert_one(objDic) #cria uma tabela e insere os dados criados no array

    db.conhecer.update_one({"codigo":2},{"$set ":{"atributoNovo":789}})#atualiza o array da tabela
    db.conecer.delete_one({"codigo":1})#deleta a tabela a partir do código selecionado
    resultadoDeConsulta=db.conhecer.find()
    for doc in resultadoDeConsulta:#vai ficar no laço até que todos os dados na variavel resultadoDeConsulta estejam finalizados
        print(doc)

manipularDadosDoMongo()
