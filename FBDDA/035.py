#Escreva um programa que leia o
#Nome, idade e sexo de 4 pessoas. No final mostre:

#A média de idade do grupo
#Qual é o homem mais velho
#Quantas mulheres têm menos de 20 anos

compatibilidade = 0
mais_velho = 0
soma = 0
for i in range(1,5):
  nome = input('Digite seu nome: ').lower()
  idade = int(input('Digite sua idade: '))
  sexo = input('Digite seu sexo: ').lower()
  soma = soma + idade
  if mais_velho == 0 and sexo == 'masculino':
   mais_velho = idade
   nome_mais_velho = nome

  if sexo == 'masculino' and mais_velho < idade:
    mais_velho = idade
    nome_mais_velho = nome


  if (sexo == 'feminino') and (idade < 20):
    compatibilidade += 1


media = soma / 4

print(f'A média etária do grupo é {media}, o homem mais velho é {nome_mais_velho} e o grupo possui {compatibilidade} mulheres com menos de 20 anos.')








