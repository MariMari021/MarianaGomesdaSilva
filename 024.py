#Escreva um programa que peça ao usuário uma senha e
# verifique se ela está correta (a senha correta é "python123").

usuario = input('Digite a senha correta: ')

if usuario == 'python123':
    print(f'Senha correta!')
else:
    print(f'Senha incorreta!')