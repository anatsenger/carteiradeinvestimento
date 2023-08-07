import requests
from validate_docbr import CPF
from datetime import datetime
def valida_cep():
    while True:
        cep = input("CEP: ")
        cep = cep.replace("-", "").replace(".", "").replace(" ", "")
        if cep.isdigit() and len(cep) == 8:
            try:
                link = f'https://viacep.com.br/ws/{cep}/json/'
                requisicao = requests.get(link)
                dic_requisicao = requisicao.json()

                endereco = {
                    "CEP": dic_requisicao['cep'],
                    "Logradouro": dic_requisicao['logradouro'],
                    "Complemento": dic_requisicao['complemento'],
                    "Bairro": dic_requisicao['bairro'],
                    "Cidade": dic_requisicao['localidade'],
                    "Estado": dic_requisicao['uf']
                }

                return endereco
            except KeyError:
                print("CEP Inválido, digite novamente:")
        else:
            print("CEP Inválido, digite novamente:")


def valida_cpf():
    cpf_validador = CPF()

    while True:
        cpf = input("CPF: ")
        resultado_validacao = cpf_validador.validate(cpf)

        if(resultado_validacao):
            # cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
            cpf = cpf.replace('.', '').replace('-', '')
            return cpf
        else:
            print("CPF inválido, digite novamente: ")

def gera_cpf():
    cpf = CPF()
    cpf_gerado = cpf.generate()
    return cpf_gerado

def valida_data():
    while True:
        data_nascimento = input("Data Nascimento: ")
        try:
            data_convertida = datetime.strptime(data_nascimento, "%d/%m/%Y").date()
            data_atual = datetime.now().date()

            if data_convertida < data_atual:
                return data_convertida.strftime("%d/%m/%Y")
            else:
                print("A data de nascimento não pode ser maior que a data atual.")
        except ValueError as e:
            print("Recebei um erro: ", e,
                  ", porém estou utilizando tratamento de erros. Digite novamente a data de nascimento.")
        finally:
            print("Fluxo de validação encerrado.")

def valida_rg():
    while True:
        rg = input("RG: ")
        rg = rg.replace('.', '').replace('-', '')

        if not rg.isdigit() or len(rg) < 8 or len(rg) > 9:
            print("RG inválido, digite novamente: ")
        else:
            rg_formatado = f"{rg[:2]}.{rg[2:5]}.{rg[5:8]}-{rg[7]}"
            return rg_formatado
