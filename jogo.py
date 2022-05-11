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

    