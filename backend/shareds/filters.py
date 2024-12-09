from dj_rql.filter_cls import AutoRQLFilterClass
from shareds.models import Endereco, Telefone, CepSourceApi


class EnderecoFilterClass(AutoRQLFilterClass):
    MODEL = Endereco

    FILTERS = [
        "cep",
        "logradouro",
        "bairro",
        "localidade",
        "uf",
        "estado",
        "regiao",
        "numero",
        "complemento",
    ]


class TelefoneFilterClass(AutoRQLFilterClass):
    MODEL = Telefone

    FILTERS = [
        "numero",
        "tipo",
    ]


class CepSourceApiFilterClass(AutoRQLFilterClass):
    MODEL = CepSourceApi

    FILTERS = [
        "cep",
        "logradouro",
        "bairro",
        "localidade",
        "uf",
        "estado",
        "regiao",
        "ibge",
        "gia",
        "ddd",
        "siafi",
        "criado_em",
    ]
