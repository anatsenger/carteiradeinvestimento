import psycopg2


class Db_cliente:
    def __init__(self):
        self.connection = psycopg2.connect(**self.retorna_parametros_conexao_banco_de_dados())
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def insert(self, tabela, cliente):
        insert_query = f"""
            INSERT INTO {tabela} (nome, cpf, rg, data_nascimento, cep, logradouro, complemento,
                bairro, cidade, estado, numero_residencia)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        values = (
            cliente['nome'],
            cliente['cpf'],
            cliente['rg'],
            cliente['data_nascimento'],
            cliente['endereco']['CEP'],
            cliente['endereco']['Logradouro'],
            cliente['endereco']['Complemento'],
            cliente['endereco']['Bairro'],
            cliente['endereco']['Cidade'],
            cliente['endereco']['Estado'],
            cliente['numero_casa']
        )
        self.cursor.execute(insert_query, values)
        self.connection.commit()

    def select(self, tabela, cpf: str):
        select_query = f"SELECT * FROM {tabela} WHERE cpf = '{cpf}';"
        self.cursor.execute(select_query)
        cliente = self.cursor.fetchall()
        return cliente

    def update(self, tabela, cliente, novo_cliente):
        update_query = f"""
            UPDATE {tabela}
            SET nome = %s, cpf = %s, rg = %s, data_nascimento = %s,
                cep = %s, logradouro = %s, complemento = %s,
                bairro = %s, cidade = %s, estado = %s, numero_residencia = %s
            WHERE cpf = %s;
        """
        values = (
            novo_cliente['nome'],
            novo_cliente['cpf'],
            novo_cliente['rg'],
            novo_cliente['data_nascimento'],
            novo_cliente['cep']['CEP'],
            novo_cliente['cep']['logradouro'],
            novo_cliente['cep']['complemento'],
            novo_cliente['cep']['bairro'],
            novo_cliente['cep']['cidade'],
            novo_cliente['cep']['estado'],
            novo_cliente['numero_casa'],
            cliente['cpf']
        )
        self.cursor.execute(update_query, values)
        self.connection.commit()

    def delete(self, tabela, cpf):
        delete_query = f"DELETE * FROM {tabela} WHERE cpf = {cpf};"
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
