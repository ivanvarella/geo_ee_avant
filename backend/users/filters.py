from dj_rql.filter_cls import AutoRQLFilterClass
from users.models import CustomUser


class UserFilterClass(AutoRQLFilterClass):
    MODEL = CustomUser

    FILTERS = [{"filter": "user", "source": "email"}]
