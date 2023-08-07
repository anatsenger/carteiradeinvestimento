from models.cliente import Cliente
from models.ordem import Ordem
import utils.funcaos_auxiliares as fa


class main():
    retorna_menu = True
    while (retorna_menu):
        adm = Cliente()
        ord = Ordem()
        print(
            "Seja bem vindo(a) ao sistema de gerenciamento de carteira de ações da Nuclea. Selecione uma das opções abaixo:")
        print("1 - Entrar na conta;")
        print("2 - Ainda nao sou cliente;")
        print("3 - Sair;")
        # def cadastro_cliente(self):
        #     print("Informe os dados do novo cliente: ")
        #     cliente = {
        #         "nome": formata_texto(input("Nome: ")),
        #         "cpf": validators.valida_cpf(),
        #         "rg": validators.valida_rg(),
        #         "data_nascimento": validators.valida_data(),
        #         "endereco": validators.valida_cep(),
        #         "numero_casa": input("Número da casa: ")
        #     }
        #     self.banco_de_dados.insert('cliente', cliente)
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            print("Informe o cpf do cliente: ")
            cliente = adm.consultar_cliente()
            if cliente is not None:
                while (opcao != "5"):
                    opcao = fa.menu_cliente(cliente)
                    if opcao == "1":
                        fa.get_option(cliente)
                    elif opcao == "2":
                        ord.cadastro_ordem(cliente)
                    elif opcao == "3":
                        ord.analise_carteira(cliente.cpf)
                    elif opcao == "4":
                        ord.obter_dados_acao()
                    elif opcao == "5":
                        retorna_menu = fa.retorna_menu_principal()
            else:
                print("Cliente nao encontrado!")
        elif opcao == "2":
            adm.cadastro_cliente()
        elif opcao == "3":
            retorna_menu = fa.retorna_menu_principal()
        else:
            print("Nao entendi, tente novamente")

if __name__ == "__main__":
    main()
