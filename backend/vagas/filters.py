from dj_rql.filter_cls import AutoRQLFilterClass
from .models import Vaga, Candidatura


class VagaFilterClass(AutoRQLFilterClass):
    MODEL = Vaga

    FILTERS = [
        "id",
        "nome",
        "descricao",
        "responsabilidades_atribuicoes",
        "requisitos_qualificacoes",
        "informacoes_adicionais",
        "sobre_empresa",
        "data_publicacao",
        "data_encerramento",
        "status",
        "modalidade",
        "pcd",
        "remuneracao",
        # Relacionamento com o modelo Empresa
        "empresa__id",
        "empresa__nome_empresa",
    ]

    SEARCH_FIELDS = [
        "nome",
        "descricao",
        "requisitos_qualificacoes",
        "sobre_empresa",
        "empresa__nome_empresa",
    ]

    FIELD_ANNOTATIONS = {
        # Configurações adicionais para relacionamento com Empresa
        "empresa__nome_empresa": {"field": "empresa__nome_empresa"},
        "empresa__cnpj": {"field": "empresa__cnpj"},
    }

    # Filtros personalizados
    @classmethod
    def filter_by_pcd(cls, qs, value):
        return qs.filter(pcd=value)

    CUSTOM_FILTERS = {
        "pcd": {"filter_func": filter_by_pcd, "type": str},
    }


class CandidaturaFilterClass(AutoRQLFilterClass):
    MODEL = Candidatura

    FILTERS = [
        "id",
        "usuario__id",
        "usuario__username",
        "vaga__id",
        "vaga__nome",
        "data_candidatura",
        "status",
    ]

    SEARCH_FIELDS = [
        "usuario__username",
        "vaga__nome",
    ]

    FIELD_ANNOTATIONS = {
        # Configurações adicionais para o relacionamento com o modelo Vaga e o usuário
        "usuario__username": {"field": "usuario__username"},
        "vaga__nome": {"field": "vaga__nome"},
    }

    # Filtro personalizado para status
    @classmethod
    def filter_by_status(cls, qs, value):
        return qs.filter(status=value)

    CUSTOM_FILTERS = {
        "status": {"filter_func": filter_by_status, "type": str},
    }
