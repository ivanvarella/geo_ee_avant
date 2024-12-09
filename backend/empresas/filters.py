from dj_rql.filter_cls import AutoRQLFilterClass
from .models import Empresa


class EmpresaFilterClass(AutoRQLFilterClass):
    MODEL = Empresa

    FILTERS = [
        "id",
        "nome_empresa",
        "email_corporativo",
        "site_empresa",
        "linkedin_empresa",
        "instagram_empresa",
        "numero_funcionarios",
        "segmento_empresa",
        "cnpj",
        "informacoes_empresa",
    ]

    SEARCH_FIELDS = [
        "nome_empresa",
        "email_corporativo",
        "segmento_empresa",
        "cnpj",
        "informacoes_empresa",
    ]

    # Configurações para campos específicos
    FIELD_ANNOTATIONS = {
        "endereco__cep": {"field": "endereco__cep"},
        "endereco__logradouro": {"field": "endereco__logradouro"},
        "endereco__bairro": {"field": "endereco__bairro"},
        "endereco__localidade": {"field": "endereco__localidade"},
        "endereco__uf": {"field": "endereco__uf"},
        "endereco__estado": {"field": "endereco__estado"},
        "endereco__regiao": {"field": "endereco__regiao"},
        "representante__id": {"field": "representante__id"},
        "representante__username": {"field": "representante__username"},
        "representante__email": {"field": "representante__email"},
    }

    # Filtros personalizados
    @classmethod
    def filter_has_logo(cls, qs, value):
        return qs.filter(logo__isnull=not value)

    @classmethod
    def filter_has_banner(cls, qs, value):
        return qs.filter(banner__isnull=not value)

    @classmethod
    def filter_telefone(cls, qs, value):
        return qs.filter(telefones__numero__icontains=value)

    # Adiciona filtros personalizados
    CUSTOM_FILTERS = {
        "has_logo": {"filter_func": filter_has_logo, "type": bool},
        "has_banner": {"filter_func": filter_has_banner, "type": bool},
        "telefone": {"filter_func": filter_telefone, "type": str},
    }
