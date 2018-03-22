from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'
    verbose_name = 'Accounts Application'
    
    def ready(self):
        from . import signals