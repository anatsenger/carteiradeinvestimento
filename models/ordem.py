from repository.db_ordem import Db_ordem
import utils.validators as validators
from datetime import datetime
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

class Ordem:

    def __init__(self):
        self.db_ordem = Db_ordem()

    # def __init__(self, acao, valor_compra, data_compra, cliente_id):
    #     self.acao = acao
    #     self.valor_compra = valor_compra
    #     self.data_compra = data_compra
    #     self.cliente_id = cliente_id
    #
    #     self.db_ordem = Db_ordem()

    def cadastro_ordem(self, cliente):
        print("Informe os dados da compra: ")
        ordem = {
            "acao": input("Nome da acao: "),
            "valor_compra": input("valor da compra: "),
            "data_compra": datetime.now(),
            "cliente_id": cliente.id,
        }
        self.db_ordem.insert('ordem', ordem)

    def consultar_ordem(self):
        cpf = validators.valida_cpf()
        return self.db_ordem.select(cpf)

    def delete_acao(self, cliente):
        print("Voce tem certeza que quer regastar todo o investido na acao? Digite o nome da acao para confirmar")
        acao = input("Acao: ")
        try:
            return self.db_ordem.delete_by_cpf(cliente, acao)
        except Exception as e:
            print('funcao nao encontrada, tente novamente')
            print(f"Detalhes do erro: {e}")
            self.delete_acao(cliente)

    # def resgatar(self, cliente):
    #     acao = input("Digite o nome da acao que deseja resgatar: ")
    #     ordens_cliente = self.select(cliente.cpf)
    #     total_acao = 0
    #     for ordem in ordens_cliente:
    #       if ordem[1] == acao:
    #           total_acao += ordem[2]
    #     print('Valor investido na acao: {total_acao}')
    #     resgate = input("Digite o valro que deseja resgatar")
    #     if resgate <= total_acao:
    #

    def analise_carteira(self, cpf):
        start_date = "2020-01-01"
        end_date = datetime.today().strftime('%Y-%m-%d')
        acoes_cliente = self.db_ordem.select(cpf)
        lista = [acao[1] + '.SA' for acao in acoes_cliente]
        df = pd.DataFrame()
        for i in lista:
            cotacao = yf.download(i, start=start_date, end=end_date)
            df[i] = cotacao['Adj Close']
        df.plot(figsize=(15, 10))
        plt.xlabel('Anos')
        plt.ylabel('Valor Ticket')
        plt.title('Variação de valor das ações')
        plt.legend()
        plt.show()

    def obter_dados_acao(self):
        ticker = input("Digite o código da ação na B3 (ex: PETR4): ").strip().upper()
        nome_arquivo = input("Digite o nome do arquivo de saída (ex: relatorio_acao.txt): ").strip()
        try:
            acao = yf.download(ticker + '.SA', progress=False)

            with open(nome_arquivo, 'w') as arquivo:
                arquivo.write("Relatorio da acao: " + ticker + "\n")
                arquivo.write(str(acao.tail()))

            print(f"Relatório exportado com sucesso para o arquivo '{nome_arquivo}'.")

        except Exception as e:
            print("Erro ao obter dados da ação. Verifique o código da ação e tente novamente.")
            print(f"Detalhes do erro: {e}")





    def __str__(self):
        return f"ID: {self.id}, Ação: {self.acao}, Valor de Compra: {self.valor_compra}, Data de Compra: {self.data_compra}, ID do Cliente: {self.cliente_id}"

