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

    bandeira = paises[pais]['bandeira']
    cores = []
    for cor, num in bandeira.items():
        if cor != 'outras' and num != 0:
            cores.append(cor)
               
    lt1 = paises[pais]['geo']['latitude']
    lg1 = paises[pais]['geo']['longitude']
    raio = 6371