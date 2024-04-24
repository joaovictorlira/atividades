lista_convidados = ['Neymar', 'Taylor Swift', 'Bob Marley', 'Gustavo Guanabara', 'Joao Lira']
for convidado in lista_convidados:  # Corrigido para 'convidado' ao invés de 'convidados'
    print(f'Você está convidado(a) para jantar na minha casa {convidado}!')
print()
print('Infelizmente o Bob Marley não poderá comparecer pois ele está morto!')

lista_convidados.remove('Bob Marley')
lista_convidados.insert(2, 'Mano Brown')
print(f'Algumas pessoas não poderão ir, mas você {lista_convidados} continuará sendo bem recebido no jantar às 19:00! ')