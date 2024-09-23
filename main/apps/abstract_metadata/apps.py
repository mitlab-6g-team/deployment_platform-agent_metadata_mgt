from django.apps import AppConfig


class AbstractMetadataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main.apps.abstract_metadata'
