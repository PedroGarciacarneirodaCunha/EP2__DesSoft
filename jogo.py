from funcoes import *
from dados import DADOS
from random import choice
from colorama import Fore, Style

paises = normaliza(DADOS)

print (
'''
 ============================ 
|                            |
| Bem-vindo ao Insper Países |
|                            |
 ==== Design de Software ==== 
'''
)

print('Comandos:')

print('''
    dica     - Entra no mercado de dicas
    desisto  - Desiste da rodada
''')

jogo = True

while jogo:
    print(
f'''
Um pais foi escolhido, tente adivinhar!
Você tem {colore_tentativas(20)} tentativas.
''')

    tentativas = 20 # tentativas disponíveis
    palpites = [] # lista com todos os palpites

    pais = sorteia_pais(paises) # Sorteia um país

    capital = paises[pais]["capital"]

    dicas = {'1':['Cor da bandeira', 4], '2':['Letra da capital', 3], '3':['Área', 6], '4':['População', 5], '5':['Continente', 7], '0':['Sem dica', 0]} ## Dicionário com as dicas disponíveis inicialmente
    
    total_d = 0 ## Total de dicas pedidas

    dicas_dadas = [] ## Lista com todas as dicas dadas

    bandeira = paises[pais]['bandeira']
    cores = []
    for cor, num in bandeira.items():
        if cor != 'outras' and num != 0:
            cores.append(cor)
               
    lt1 = paises[pais]['geo']['latitude']
    lg1 = paises[pais]['geo']['longitude']
    raio = 6371

    restritos = restringe(capital) # Lista de letras restritas no sorteio

    while tentativas > 0:

        palpite = input('Qual o seu palpite? ').lower()

        na_lista = esta_na_lista(palpite, palpites)

        if not na_lista:

            if palpite == 'dica':

                if total_d == 4:

                    print('>>>> Você não tem mais dicas')
                
                else :

                    dica_l = ldicas(dicas)

                    print ('Mercado de dicas')
                    print ('------------------------------------------')

                    for opt in dica_l:

                        print(opt)

                    print('------------------------------------------')

                    disp = func_disp(dicas)

                    o = input(f' Escolha uma dica {disp}: ')

                    while o not in dicas.keys():

                        print ('Opção inválida')
                        o = input(f'Escolha uma dica {disp}: ')
                    
                    if dicas[o][1] > tentativas:

                        print ('Você não tem tentativas suficiente')

                    else:
                        if o == '1':

                            car_sort = choice(cores)
                            
                            dicas_dadas.append(f'Cores da bandeira: {car_sort}')

                            cores.remove (car_sort)

                            if len (cores) == 0:

                                del dicas [o]

                            tentativas -= 4

                            total_d += 1

                        elif o == '2':

                            capital = paises[pais]['capital']

                            sorteado = sorteia_letra(capital, restritos)

                            restritos.append(sorteado)

                            dicas_dadas.append(f'Letra de capital: {sorteado}')

                            tentativas -= 3

                            total_d += 1

                        elif o == '3':

                            area = paises[pais]['area'] / 1000

                            dicas_dadas.append(f'Área: {area} km2')

                            tentativas -= 6

                            del dicas[o]

                            total_d += 1

                        elif o == '4':

                            pop = paises[pais]['populacao']

                            dicas_dadas.append(f'População: {pop} habitantes')

                            tentativas -= 5

                            del dicas [o]

                            total_d += 1

                        elif o == '5':

                            cont = paises[pais]['continente']

                            dicas_dadas.append(f'Continente: {cont}')

                            tentativas -= 7

                            del dicas [o]

                            total_d += 1

                        print('Distâncias: ')

                        for chute in palpites:

                            print(f'{colore_palavra(chute)}')

                        print ('Dicas: ')

                        for dica in dicas_dadas:

                            print(dica)

                        if tentativas > 0:

                            print (f'Você ainda tem { colore_tentativas(tentativas)} tentativas(s)')

                        


            elif palpite == 'desisto':
                print('Calma, o senhor está nervoso')
                ctz = input('Tem certeza que deseja desistir da rodada? [s|n] ')
                while ctz != 's' and ctz != 'n':
                    ctz = input('Digite |s| ou |n|: ')
                if ctz == 's':
                    print(f'Você perdeu, o país era: {pais}')
                    break
            
            elif palpite == pais:
                print (f'Parabéns, você acertou em {20 - tentativas + 1} tentativa(s)!!!')
                break

            elif palpite not in paises.keys():
                print('País desconecido')

            elif palpite != 'dica' and palpite != 'desisto':
                lt2 = paises[palpite]['geo']['latitude']
                lg2 = paises[palpite]['geo']['longitude']

                distancia = haversine(raio, lt1, lg1, lt2, lg2) / 1000

                # Adiciona o palpite na lista de países citados
                palpites = adiciona_em_ordem(palpite, distancia, palpites)

                print ('Distâncias: ')

                for chute in palpites:

                    print(f'{colore_palavra(chute)}')

                print ('Dicas: ')

                for dica in dicas_dadas:

                    print(dica)

                tentativas -= 1

                if tentativas > 0:

                    print (f'Você ainda tem { colore_tentativas(tentativas)} teantativa(s)')

    if tentativas == 0:

        print (f'Você perdeu, o país era: {pais}')

    jogar = input ('Jogar novamente? [s|n] ')

    while jogar != 's' and jogar != 'n':

        jogar = input ('Digite |s| ou |n|: ')

    if jogar == 'n':

        print ('Até a próxima!')

        break