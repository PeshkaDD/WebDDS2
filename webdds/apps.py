# dds/apps.py
from django.apps import AppConfig

class DdsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'webdds'

    def ready(self):
        from django.db.models.signals import post_migrate
        from .signals import create_initial_data
        post_migrate.connect(create_initial_data, sender=self)