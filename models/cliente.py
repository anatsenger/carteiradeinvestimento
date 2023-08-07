from repository.db_client import Db_cliente
from utils.funcaos_auxiliares import formata_texto
import utils.validators as validators


class Cliente:

    def __init__(self, id=None, nome=None, cpf=None, rg=None, data_nascimento=None, cep=None, logradouro=None, complemento=None,
                 bairro=None, cidade=None, estado=None, numero_residencia=None):
        if id is not None:
            self.id = id
        if nome is not None:
            self.nome = nome
        if cpf is not None:
            self.cpf = cpf
        if rg is not None:
            self.rg = rg
        if data_nascimento is not None:
            self.data_nascimento = data_nascimento
        if cep is not None:
            self.cep = cep
        if logradouro is not None:
            self.logradouro = logradouro
        if complemento is not None:
            self.complemento = complemento
        if bairro is not None:
            self.bairro = bairro
        if cidade is not None:
            self.cidade = cidade
        if estado is not None:
            self.estado = estado
        if numero_residencia is not None:
            self.numero_residencia = numero_residencia

        self.banco_de_dados = Db_cliente()

    @classmethod
    def criar_cliente(cls, dados_cliente):
        return cls(
            id=dados_cliente[0],
            nome=dados_cliente[1],
            cpf=dados_cliente[2],
            rg=dados_cliente[3],
            data_nascimento=dados_cliente[4],
            cep=dados_cliente[5],
            logradouro=dados_cliente[6],
            complemento=dados_cliente[7],
            bairro=dados_cliente[8],
            cidade=dados_cliente[9],
            estado=dados_cliente[10],
            numero_residencia=dados_cliente[11]
        )

    def cadastro_cliente(self):
        print("Informe os dados do novo cliente: ")
        cliente = {
            "nome": formata_texto(input("Nome: ")),
            "cpf": validators.valida_cpf(),
            "rg": validators.valida_rg(),
            "data_nascimento": validators.valida_data(),
            "endereco": validators.valida_cep(),
            "numero_casa": input("Número da casa: ")
        }
        self.banco_de_dados.insert('cliente', cliente)

    def consultar_cliente(self):
        cpf = validators.valida_cpf()
        dados_cliente = self.banco_de_dados.select('cliente', cpf)
        print(dados_cliente)
        if dados_cliente:
            dados_cliente_list = list(dados_cliente[0])
            return self.criar_cliente(dados_cliente_list)
        else:
            return None

    def alterar_cliente(self, cliente):
        cliente_alterado = {
            "nome": formata_texto(input("Nome: ")),
            "cpf": validators.valida_cpf(),
            "rg": validators.valida_rg(),
            "data_nascimento": validators.valida_data(),
            "endereco": validators.valida_cep(),
            "numero_casa": input("Número da casa: ")
        }
        self.banco_de_dados.update('cliente', cliente, cliente_alterado)

    def delete_cliente(self):
        print("Voce tem certeza que quer deletar a sua conta? Digite seu cpf para confirmar:")
        cpf = validators.valida_cpf()
        return self.banco_de_dados.delete('cliente', cpf)

    def to_dict(self):
        return {
            "nome": self.nome,
            "cpf": f"{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}",
            "rg": self.rg,
            "data_nascimento": self.data_nascimento,
            "cep": self.cep,
            "logradouro": self.logradouro,
            "complemento": self.complemento,
            "bairro": self.bairro,
            "cidade": self.cidade,
            "estado": self.estado,
            "numero_residencia": self.numero_residencia
        }

