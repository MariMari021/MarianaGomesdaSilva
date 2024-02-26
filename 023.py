#Escreva um programa que peça ao usuário uma palavra e
# imprima se começa com vogal ou consoante.

usuario = input('Insira uma palavra: ').upper()

if usuario[0] in 'AEIOU':
    print(f'A palavra começa com uma vogal!')
else:
    print(f'A palavra começa com uma consoante!')