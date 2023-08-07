import unittest
from unittest.mock import patch

from faker import Faker


from main import main
from models.cliente import Cliente
from utils.validators import gera_cpf


class TestClients(unittest.TestCase):
    def gerar_nome_fake(self):
        fake = Faker()
        return fake.name()


    def test_cadastro_cliente_with_fake_client_should_return_correct_client(self):
        cliente = Cliente()
        nome = self.gerar_nome_fake()
        print(nome)
        cpf = gera_cpf()
        print(cpf)
        inputs_cadastro = ["2", nome, cpf, "22.775.406-2", "12/02/2001", "20211-972", "426", "3", "nao"]

        with patch("builtins.input", side_effect=inputs_cadastro):
            main()

        inputs_consulta = [f"'{cpf}'"]
        with patch("builtins.input", side_effect=inputs_consulta):
            client_list = cliente.consultar_cliente()

        self.assertGreater(len(client_list), 1)
        self.assertTrue(client_list[2] == cpf)
