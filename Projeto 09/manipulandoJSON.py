import urllib.request
import urllib.request
import json        #necessário para poder controlar arquivos do tipo json

def manipularJson():
    endereco="http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    webUrl=urllib.request.urlopen(endereco)
    if(webUrl.getcode()==200):      #pega as linhas de código da url
        dados=webUrl.read()         #lendo dados da url
        oJSON=json.loads(dados)     #carregando ods dados do json
        pass

    contagem= oJSON["metadata"]["count"]#contagem recebe arquivo JSON metadata tudo relacionado ao count
    print("contagem :"+str(contagem))
    for local in oJSON["features"]:#vai imprimir todo o array que esta em features
        print(local["properties"]["place"])