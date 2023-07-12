def valid_cpf(cpf_):
    return len(cpf_) == 11

def valid_rg(rg_):
    return len(rg_) == 9

def valid_name(name_):
    return name_.isalpha()

def valid_cellphone(cellphone_):
    return len(cellphone_) > 11
