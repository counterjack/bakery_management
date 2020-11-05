from django.apps import AppConfig
# from project.bakery.signals

class BakeryConfig(AppConfig):
    name = 'bakery'

    def ready(self):
        import bakery.signals
