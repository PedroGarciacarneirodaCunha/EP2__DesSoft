from funcoes import *
from dados import DADOS

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
'''
Um pais foi escolhido, tente adivinhar!
Você tem 20 tentativas.
''')

    tentativas = 20 # tentativas disponíveis
    palpites = [] # lista com todos os palpites

    pais = sorteia_pais(paises) # Sorteia um país

    capital = paises[pais]["capital"]

    dicas = {'1':['Cor da bandeira', 4], '2':['Letra da capital', 3], '3':['Área', 6], '4':['População', 5], '5':['Continente', 7], '0':['Sem dica', 0]}} ## Dicionário com as dicas disponíveis inicialmente
    
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

            if palpite == 'desisto':
                print('Calma, o senhor está nervoso')
                ctz = input('Tem certeza que deseja desistir da rodada? [s|n] ')
                while ctz != 's' and ctz != 'n':
                    ctz = input('Digite |s| ou |n|: ')
                if ctz == 's':
                    print(f'Você perdeu, o país era: {pais}')
                    break
            
            elif palpite == pais:
                print (f'Parabésn, você acertou em {20 - tentativas + 1} tentativa(s)!!!')
                break

            elif palpite not in paises.keys():
                print('País desconecido')

            elif palpite != 'dica' and palpite != 'desisto':
                lt2 = paises[palpite]['geo']['latitude']
                lg2 = paises[palpite]['geo']['longitude']

                distancia = haversine(raio, lt1, lg1, lt2, lg2) / 1000

                # Adiciona o palpite na lista de países citados
                palpites = adiciona_em_ordem(palpite, distancia, palpites)