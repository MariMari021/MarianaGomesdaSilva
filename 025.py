#Crie um programa para jogar JOKEMPO, usando a função random.randint


# pedra: 1
# papel: 2
# tesoura: 3

usuario = int(input('Pedra(1), Papel(2) ou Tesoura(3): '))

import random

computador = random.randint(1,3)
print(computador)
if (usuario == 1) and (computador == 1):
    print(f'Empate')
elif (usuario == 2) and (computador == 2):
    print(f'Empate')
elif (usuario == 3) and (computador == 3):
    print(f'Empate')
elif (usuario == 1) and (computador == 2):
    print(f'Computador venceu!')
elif (usuario == 1) and (computador == 3):
    print(f'Usuário venceu!')
elif (usuario == 2 ) and (computador == 1):
    print(f'Usuário venceu!')
elif (usuario == 2 ) and (computador == 3):
    print(f'Computador venceu!')
elif (usuario == 3 ) and (computador == 1):
    print(f'Computador venceu!')
elif (usuario == 3 ) and (computador == 2):
    print(f'Usuario venceu!')
else:
    print(f'Opção inválida!')


