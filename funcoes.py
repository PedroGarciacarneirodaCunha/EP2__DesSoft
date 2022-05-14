from random import choice
from math import *
from colorama import Fore, Back, Style
from more_itertools import pairwise

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

    saida = dicas_disp.replace(', ', '|')

    return saida

# Criando a lista de letras restirtas (usada no "Sorteando a letra")

def restringe(nome):

    saida = []
    
    aux = {}

    for letra in nome:

        if letra not in aux.keys():

            aux[letra] = 1
        else:

            aux[letra] += 1

    for letra, rep in aux.items():

        if rep > 1:
            saida.append(letra)

    return saida

# Colorindo as distancias

def colore_palavra(lista):

    pais = lista[0]
    
    dist = lista[1]

    if dist >= 10.000:

        saida = (Fore.BLACK + f'{lista[1]:.3f} km -> {lista[0]}' + Style.RESET_ALL)
    
    elif dist >= 4.000:
        
        saida = (Fore.RED + f'{lista[1]:.3f} km -> {lista[0]}' + Style.RESET_ALL)

    elif dist >= 1.000:

        saida = (Fore.YELLOW + f'{lista[1]:.3f} km -> {lista[0]}' + Style.RESET_ALL)

    else:

        saida = (Fore.BLUE + f'{int(lista[1] * 1000)} km -> {lista[0]}' + Style.RESET_ALL)
    
    return saida

# Colorindo o número de tentativas

def colore_tentativas(num):

    if num > 10:

        return (Fore.BLUE + f'{num}' + Style.RESET_ALL)
    
    elif num > 5:

        return (Fore.YELLOW + f'{num}' + Style.RESET_ALL)

    else:

        return (Fore.RED + f'{num}' + Style.RESET_ALL)

