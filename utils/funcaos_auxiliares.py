
def retorna_menu_principal():
    retorna_menu_principal = input("Deseja retornar ao menu principal? (sim/não) ")
    if retorna_menu_principal == "sim":
        return True
    elif retorna_menu_principal == "nao":
        return False

def formata_texto(texto):
    nome_formatado = texto.title()
    return nome_formatado

def menu_cliente(cliente):
    print(f"Bem vindo a sua carteira {cliente.nome}")
    print('1- Opcoes de perfil')
    print('2- Cadastrar acao')
    print('3- Realizar analise da carteira')
    print('4- Imprimir relatorio da carteira')
    print('5- Sair')
    opcao = input("Digite a opção desejada: ")
    return opcao
def opcoes_perfil():
    print('1- Consultar dados de conta')
    print('2- Alterar dados')
    print('3- Deletar conta')
    print('4- Sair da conta')
    opcao = input("Digite a opção desejada: ")
    return opcao


def get_option(cliente):
    opcao = opcoes_perfil()
    if opcao == "1":
        print(cliente.to_dict())
    elif opcao == "2":
        cliente.alterar_cliente(cliente)
    elif opcao == "3":
        cliente.delete_cliente()
    elif opcao == "4":
        print("saindoo")
        return retorna_menu_principal()
    else:
        get_option(cliente)


