import re

from validate_docbr import CPF


def valid_cpf(cpf_):
    cpf = CPF()
    return cpf.validate(cpf_)

def valid_rg(rg_):
    return len(rg_) == 9

def valid_name(name_):
    return name_.isalpha()

def valid_cellphone(cellphone_):
    model = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    verified = re.findall(model, cellphone_)
    return verified
