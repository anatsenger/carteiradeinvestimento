import psycopg2
import os

class Db_ordem:
    def __init__(self):
        self.connection = psycopg2.connect(**self.retorna_parametros_conexao_banco_de_dados())
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def insert(self, cliente, ordem):
        insert_query = f"""
            INSERT INTO ordem (acao, valor_compra, data_compra, cliente_id)
            VALUES (%s, %s, %s, %s);
        """
        values = (
            ordem['acao'],
            ordem['valor_compra'],
            ordem['data_compra'],
            ordem['cliente_id'],
        )
        self.cursor.execute(insert_query, values)
        self.connection.commit()

    def select(self, cpf):
        select_query = f"SELECT ordem.id, ordem.acao, ordem.valor_compra, ordem.cliente_id " \
                       f"FROM ordem JOIN cliente ON ordem.cliente_id = cliente.id " \
                       f"WHERE cliente.cpf = '{cpf}';"
        self.cursor.execute(select_query)
        ordem = self.cursor.fetchall()
        return ordem

    def delete(self, id):
        delete_query = f"DELETE * FROM ORDEM WHERE id = {id};"
        self.cursor.execute(delete_query)
        self.connection.commit()

    def delete_by_cpf(self, cliente, acao):
        delete_query = f"DELETE ordem " \
                       f"FROM ordem " \
                       f"JOIN cliente ON ordem.cliente_id = cliente.id " \
                       f"WHERE cliente.cpf = {cliente.cpf} AND ordem.acao = {acao};"
        self.cursor.execute(delete_query)
        self.connection.commit()


    @staticmethod
    def retorna_parametros_conexao_banco_de_dados():
        parametros_conexao = {
            "user": 'postgres',
            "password": '1234',
            "host": 'localhost',
            "port": '5432',
            "database": 'nuclea'
        }

        return parametros_conexao