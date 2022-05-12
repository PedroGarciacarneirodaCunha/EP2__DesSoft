from random import choice
from math import *

def normaliza(dic):
    saida = {}
    for continente, paises in dic.items():
        for pais, infos in paises.items():
            saida[pais] = infos
            saida[pais]['continente'] = continente
    return saida


# Calcula distancia entre dois países
def haversine(r, lt1, lg1, lt2, lg2):
    termo1 = 2 * r
    termo2 = (sin(radians(lt2 - lt1) / 2))**2
    termo3 = cos(radians(lt1)) * cos(radians(lt2))
    termo4 = (sin(radians(lg2 - lg1) / 2))**2

    d = termo1 * asin(sqrt(termo2 + termo3 * termo4))

    return d

# Sorteia país
def sorteia_pais(paises):
    lista = []
    for pais in paises.keys():
        lista.append(pais)
    
    pais = choice(lista)

    return pais