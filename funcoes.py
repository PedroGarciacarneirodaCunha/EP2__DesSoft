from random import choice
from math import *

# Corrigir o dicionario
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

# Colocando as distâncias em ordem
def adiciona_em_ordem (pais, distancia, lista):

    saida = []

    combonovo = [pais, distancia]

    if len (lista) == 0:

        saida.append (combonovo)

        return saida
    
    for i in lista:

        paises = i[0]

        dist = i[1]

        combo = [paises, dist]

        if distancia > dist:

            saida.append(combo)

        elif distancia < dist and [pais, distancia] not in saida:

            saida.append (combonovo)

            saida.append (combo)

        else:

            saida.append(combo)

    if [pais, distancia] not in saida:

        saida.append(combonovo)

    return saida

# Analisando se o país já foi citado

def esta_na_lista (pais, paises):

    for i in paises:

        if pais == i[0]:

            return True
            
    return False

# Sorteando a letra

def sorteia_letra(palavra, restritos):

    palavra = palavra.lower()

    especiais = ['.', ',', '-', ';', ' ']

    lista = []

    for letra in palavra:

        if letra not in especiais and letra not in restritos:

            lista.append(letra)

    if len(lista) == 0:

        return ''

    sorteado = choice(lista)

    return sorteado

# Fazendo a lista de dicas
def ldicas(dic):

    lista = []

    for valor, dica in dic.items():

        lista.append(f'{valor}. {dica[0]} - custa {dica[1]} tentativas')

    return lista

# Criando a lista de dicas disponíveis

def func_disp(dic):

    disp = []

    for val in dic.keys():
        
        val = int(val)

        disp.append(val)

    dicas_disp = f'{disp}'

    saida = dicas_disp.replace(',', '|')

    return saida

# 