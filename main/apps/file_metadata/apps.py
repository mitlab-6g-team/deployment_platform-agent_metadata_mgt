from django.apps import AppConfig


class FileMetadataConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main.apps.file_metadata'
    
    def ready(self):
        import main.apps.file_metadata.services.delete_signals
