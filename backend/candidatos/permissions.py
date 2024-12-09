from rest_framework.permissions import BasePermission, SAFE_METHODS


class DadosCandidatoPermission(BasePermission):
    """
    Permissões customizadas para o endpoint DadosCandidato:
    - Usuários do tipo candidato, quando autenticados, só podem listar e modificar seus próprios dados.
    - Somente candidatos autenticados podem criar novos dados.
    - Outros usuários autenticados podem apenas listar dados de candidatos.
    - Acesso permitido apenas para usuários autenticados.
    """

    def has_permission(self, request, view):
        user = request.user

        # Verifica se o usuário está autenticado - Evita o erro de tentar acessar sem autenticação
        if not user.is_authenticated:
            return False

        # Para visualização: Se tipo candidato -> Somente seus dados / Se outros tipos de usuários -> Todos os dados
        if request.method in SAFE_METHODS and view.action == "list":
            return user.is_authenticated

        # Apenas candidatos podem criar dados (POST)
        if request.method == "POST" and view.action == "create":
            return user.tipo == "candidato"

        # Outros métodos (PUT, PATCH, DELETE) não são permitidos para usuários que não sejam "candidato"
        if request.method not in SAFE_METHODS and user.tipo != "candidato":
            return False

        return user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Para visualização: Se tipo candidato -> Somente seus dados / Se outros tipos de usuários -> Todos os dados
        if request.method in SAFE_METHODS and view.action == "list":
            if user.tipo == "candidato":
                return obj.usuario == user
            return user.is_authenticated

        # Somente o próprio candidato pode modificar seus dados
        return obj.usuario == user


class HabilidadePermission(BasePermission):
    """
    Permissões customizadas para o endpoint DadosCandidato:
    - Usuários do tipo candidato, quando autenticados, só podem listar e modificar seus próprios dados.
    - Somente candidatos autenticados podem criar novos dados.
    - Outros usuários autenticados podem apenas listar dados de candidatos.
    - Acesso permitido apenas para usuários autenticados.
    """

    def has_permission(self, request, view):
        user = request.user

        # Verifica se o usuário está autenticado - Evita o erro de tentar acessar sem autenticação
        if not user.is_authenticated:
            return False

        # Para visualização: Se tipo candidato -> Somente seus dados / Se outros tipos de usuários -> Todos os dados
        if request.method in SAFE_METHODS and view.action == "list":
            return user.is_authenticated

        # Apenas candidatos podem criar dados (POST)
        if request.method == "POST" and view.action == "create":
            return user.tipo == "candidato"

        # Outros métodos (PUT, PATCH, DELETE) não são permitidos para usuários que não sejam "candidato"
        if request.method not in SAFE_METHODS and user.tipo != "candidato":
            return False

        return user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Para visualização: Se tipo candidato -> Somente seus dados / Se outros tipos de usuários -> Todos os dados
        if request.method in SAFE_METHODS and view.action == "list":
            if user.tipo == "candidato":
                return obj.usuario == user
            return user.is_authenticated

        # Somente o próprio candidato pode modificar seus dados
        return obj.usuario == user


class ExperienciaAcademicaPermission(BasePermission):
    """
    Permissões customizadas para o endpoint DadosCandidato:
    - Usuários do tipo candidato, quando autenticados, só podem listar e modificar seus próprios dados.
    - Somente candidatos autenticados podem criar novos dados.
    - Outros usuários autenticados podem apenas listar dados de candidatos.
    - Acesso permitido apenas para usuários autenticados.
    """

    def has_permission(self, request, view):
        user = request.user

        # Verifica se o usuário está autenticado - Evita o erro de tentar acessar sem autenticação
        if not user.is_authenticated:
            return False

        # Para visualização: Se tipo candidato -> Somente seus dados / Se outros tipos de usuários -> Todos os dados
        if request.method in SAFE_METHODS and view.action == "list":
            return user.is_authenticated

        # Apenas candidatos podem criar dados (POST)
        if request.method == "POST" and view.action == "create":
            return user.tipo == "candidato"

        # Outros métodos (PUT, PATCH, DELETE) não são permitidos para usuários que não sejam "candidato"
        if request.method not in SAFE_METHODS and user.tipo != "candidato":
            return False

        return user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Para visualização: Se tipo candidato -> Somente seus dados / Se outros tipos de usuários -> Todos os dados
        if request.method in SAFE_METHODS and view.action == "list":
            if user.tipo == "candidato":
                return obj.usuario == user
            return user.is_authenticated

        # Somente o próprio candidato pode modificar seus dados
        return obj.usuario == user


class ExperienciaProfissionalPermission(BasePermission):
    """
    Permissões customizadas para o endpoint DadosCandidato:
    - Usuários do tipo candidato, quando autenticados, só podem listar e modificar seus próprios dados.
    - Somente candidatos autenticados podem criar novos dados.
    - Outros usuários autenticados podem apenas listar dados de candidatos.
    - Acesso permitido apenas para usuários autenticados.
    """

    def has_permission(self, request, view):
        user = request.user

        # Verifica se o usuário está autenticado - Evita o erro de tentar acessar sem autenticação
        if not user.is_authenticated:
            return False

        # Para visualização: Se tipo candidato -> Somente seus dados / Se outros tipos de usuários -> Todos os dados
        if request.method in SAFE_METHODS and view.action == "list":
            return user.is_authenticated

        # Apenas candidatos podem criar dados (POST)
        if request.method == "POST" and view.action == "create":
            return user.tipo == "candidato"

        # Outros métodos (PUT, PATCH, DELETE) não são permitidos para usuários que não sejam "candidato"
        if request.method not in SAFE_METHODS and user.tipo != "candidato":
            return False

        return user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Para visualização: Se tipo candidato -> Somente seus dados / Se outros tipos de usuários -> Todos os dados
        if request.method in SAFE_METHODS and view.action == "list":
            if user.tipo == "candidato":
                return obj.usuario == user
            return user.is_authenticated

        # Somente o próprio candidato pode modificar seus dados
        return obj.usuario == user


class IdiomaPermission(BasePermission):
    """
    Permissões customizadas para o endpoint DadosCandidato:
    - Usuários do tipo candidato, quando autenticados, só podem listar e modificar seus próprios dados.
    - Somente candidatos autenticados podem criar novos dados.
    - Outros usuários autenticados podem apenas listar dados de candidatos.
    - Acesso permitido apenas para usuários autenticados.
    """

    def has_permission(self, request, view):
        user = request.user

        # Verifica se o usuário está autenticado - Evita o erro de tentar acessar sem autenticação
        if not user.is_authenticated:
            return False

        # Para visualização: Se tipo candidato -> Somente seus dados / Se outros tipos de usuários -> Todos os dados
        if request.method in SAFE_METHODS and view.action == "list":
            return user.is_authenticated

        # Apenas candidatos podem criar dados (POST)
        if request.method == "POST" and view.action == "create":
            return user.tipo == "candidato"

        # Outros métodos (PUT, PATCH, DELETE) não são permitidos para usuários que não sejam "candidato"
        if request.method not in SAFE_METHODS and user.tipo != "candidato":
            return False

        return user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Para visualização: Se tipo candidato -> Somente seus dados / Se outros tipos de usuários -> Todos os dados
        if request.method in SAFE_METHODS and view.action == "list":
            if user.tipo == "candidato":
                return obj.usuario == user
            return user.is_authenticated

        # Somente o próprio candidato pode modificar seus dados
        return obj.usuario == user


class ConquistaPermission(BasePermission):
    """
    Permissões customizadas para o endpoint DadosCandidato:
    - Usuários do tipo candidato, quando autenticados, só podem listar e modificar seus próprios dados.
    - Somente candidatos autenticados podem criar novos dados.
    - Outros usuários autenticados podem apenas listar dados de candidatos.
    - Acesso permitido apenas para usuários autenticados.
    """

    def has_permission(self, request, view):
        user = request.user

        # Verifica se o usuário está autenticado - Evita o erro de tentar acessar sem autenticação
        if not user.is_authenticated:
            return False

        # Para visualização: Se tipo candidato -> Somente seus dados / Se outros tipos de usuários -> Todos os dados
        if request.method in SAFE_METHODS and view.action == "list":
            return user.is_authenticated

        # Apenas candidatos podem criar dados (POST)
        if request.method == "POST" and view.action == "create":
            return user.tipo == "candidato"

        # Outros métodos (PUT, PATCH, DELETE) não são permitidos para usuários que não sejam "candidato"
        if request.method not in SAFE_METHODS and user.tipo != "candidato":
            return False

        return user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Para visualização: Se tipo candidato -> Somente seus dados / Se outros tipos de usuários -> Todos os dados
        if request.method in SAFE_METHODS and view.action == "list":
            if user.tipo == "candidato":
                return obj.usuario == user
            return user.is_authenticated

        # Somente o próprio candidato pode modificar seus dados
        return obj.usuario == user


class CurriculoPermission(BasePermission):
    """
    Permissões customizadas para o endpoint DadosCandidato:
    - Usuários do tipo candidato, quando autenticados, só podem listar e modificar seus próprios dados.
    - Somente candidatos autenticados podem criar novos dados.
    - Outros usuários autenticados podem apenas listar dados de candidatos.
    - Acesso permitido apenas para usuários autenticados.
    """

    def has_permission(self, request, view):
        user = request.user

        # Verifica se o usuário está autenticado - Evita o erro de tentar acessar sem autenticação
        if not user.is_authenticated:
            return False

        # Para visualização: Se tipo candidato -> Somente seus dados / Se outros tipos de usuários -> Todos os dados
        if request.method in SAFE_METHODS and view.action == "list":
            return user.is_authenticated

        # Apenas candidatos podem criar dados (POST)
        if request.method == "POST" and view.action == "create":
            return user.tipo == "candidato"

        # Outros métodos (PUT, PATCH, DELETE) não são permitidos para usuários que não sejam "candidato"
        if request.method not in SAFE_METHODS and user.tipo != "candidato":
            return False

        return user.is_authenticated

    def has_object_permission(self, request, view, obj):
        user = request.user

        # Para visualização: Se tipo candidato -> Somente seus dados / Se outros tipos de usuários -> Todos os dados
        if request.method in SAFE_METHODS and view.action == "list":
            if user.tipo == "candidato":
                return obj.usuario == user
            return user.is_authenticated

        # Somente o próprio candidato pode modificar seus dados
        return obj.usuario == user
