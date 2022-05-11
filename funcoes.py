  from random import choice

def normaliza(dic):
    saida = {}
    for continente, paises in dic.items():
        for pais, infos in paises.items():
            saida[pais] = infos
            saida[pais]['continente'] = continente
    return saida


""""# completar
def haversine (raio, latitude_1, longitude_1, latitude_2, longitude_1):

    d = 

    return d""""