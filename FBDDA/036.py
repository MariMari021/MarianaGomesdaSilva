#Escreva um programa que leia o peso de 7 pessoas, e no final,
# mostre qual foi o maior e o menor peso lidos


maior_peso = 0

for i in range(1, 8):
   peso = int(input('Digite seu peso: '))

   if peso > maior_peso:
      maior_peso = peso

   if i == 1:
      peso_ref = peso

   if peso < peso_ref:
      menor_peso = peso




print(f'o menor peso é {menor_peso} e o maior peso é {maior_peso}')
