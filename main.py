from projeto_python_skyone.Colaboradores import Colaborador
from projeto_python_skyone.Devs import Dev
from projeto_python_skyone.Squads import Squad


print('\n-==-=-=-=-=-=-=-=-=-=-=-Sky.One Solutions=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('Bem vindo ao sistema de cadastro de squads!\n')

# Estrutura para cadastrar squads enquanto o usuário digitar Sim
while True:
    squads = []
    nome_squad = input('\nNome da squad: ')
    nome_techlead = input('Nome do Techlead: ')
    fone_techlead = input('Fone do Techlead: ')

    squad = Squad(nome_squad)
    techlead = Colaborador(nome_techlead, fone_techlead)
    squad.incluir_techlead(techlead)
    techlead.incluir_squad(squad)

    squads.append(squad)

    # Estrutura para cadastrar devs dentro da squad enquanto o usuário digitar Sim
    while True:
        nome_dev = input('\nNome do desenvolvedor: ')
        fone_dev = input('Telefone do desenvolvedor: ')
        cargo_dev = input('Cargo do desenvolvedor: ')
        dev = Dev(nome_dev,fone_dev, cargo_dev)
        dev.incluir_squad(squad)
        squad.incluir_dev(dev)

        option = input('\nDeseja adicionar mais um dev [S/N]: ')
        if option in 'Nn':
            break

    option = input('\nDeseja adicionar mais uma squad [S/N]: ')
    if option in 'Nn':
        break

print('\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print('\nSquads criadas: ')

for squad in squads:
    print(f'\n------------------------------{squad.nome}------------------------------')
    print(f'Techlead: {squad.techlead.nome}')
    print('\n-----Devs do squad-----')
    for dev in squad.devs:
        dev.exibir()
    print(f'------------------------------{squad.nome}------------------------------')

print('\n-==-=-=-=-=-=-=-=-=-=-=-Sky.One Solutions=-=-=-=-=-=-=-=-=-=-=-=-=-')
