from django.apps import AppConfig
class MyappConfig(AppConfig):
    name = 'DjangoSignalApp'

    def ready(self):
        from . import signals