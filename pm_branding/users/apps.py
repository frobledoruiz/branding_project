from django.apps import AppConfig
from django.contrib.postgres import signals


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
