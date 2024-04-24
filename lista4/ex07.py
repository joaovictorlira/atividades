usuarios = []
while True:
    nome = input('Digite o nome do usuário (ou "sair" para encerrar o cadastro): ')
    if nome.lower() == 'sair':
        break

    idade = input('Digite a idade do usuário: ')
    email = input('Digite o email do usuário: ')

    usuario = {
        'nome': nome,
        'idade': idade,
        'email': email
    }
    usuarios.append(usuario)

print('Usuários cadastrados:')
for usuario in usuarios:
    print(f"Nome: {usuario['nome']}, Idade: {usuario['idade']} Email: {usuario['email']} ")
