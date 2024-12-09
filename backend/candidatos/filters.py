from dj_rql.filter_cls import AutoRQLFilterClass
from candidatos.models import (
    DadosCandidato,
    Habilidade,
    ExperienciaAcademica,
    ExperienciaProfissional,
    Idioma,
    Conquista,
    Curriculo,
)


class DadosCandidatoFilterClass(AutoRQLFilterClass):
    MODEL = DadosCandidato

    FILTERS = [
        "genero",
        "deficiencia",
        "tipo_deficiencia",
        "linkedin",
        "github",
    ]


class HabilidadeFilterClass(AutoRQLFilterClass):
    MODEL = Habilidade

    FILTERS = [
        "nome",
    ]


class ExperienciaAcademicaFilterClass(AutoRQLFilterClass):
    MODEL = ExperienciaAcademica

    FILTERS = [
        "formacao",
        "curso",
        "status",
        "instituicao",
        "inicio",
        "fim",
    ]


class ExperienciaProfissionalFilterClass(AutoRQLFilterClass):
    MODEL = ExperienciaProfissional

    FILTERS = [
        "empresa",
        "cargo",
        "atual",
        "inicio",
        "fim",
        "descricao_atividades",
    ]


class IdiomaFilterClass(AutoRQLFilterClass):
    MODEL = Idioma

    FILTERS = [
        "idioma",
        "nivel",
    ]


class ConquistaFilterClass(AutoRQLFilterClass):
    MODEL = Conquista

    FILTERS = [
        "titulo",
        "descricao",
    ]


class CurriculoFilterClass(AutoRQLFilterClass):
    MODEL = Curriculo

    FILTERS = [
        "titulo_curriculo",
        "data_envio",
    ]
