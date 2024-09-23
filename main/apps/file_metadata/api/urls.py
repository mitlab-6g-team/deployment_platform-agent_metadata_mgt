from django.urls import path
from main.utils.config import config
from main.apps.file_metadata.actors import ModelMetadataWriter

FILE_METADATA_NAME=config.FILE_METADATA.NAME

urlpatterns = [
        path(
            f'{FILE_METADATA_NAME}/ModelMetadataWriter/create',
            ModelMetadataWriter.create
            ),
        path(
            f'{FILE_METADATA_NAME}/ModelMetadataWriter/retrieve',
            ModelMetadataWriter.retrieve
            ),
        path(
            f'{FILE_METADATA_NAME}/ModelMetadataWriter/update',
            ModelMetadataWriter.update
            ),
        path(
            f'{FILE_METADATA_NAME}/ModelMetadataWriter/delete',
            ModelMetadataWriter.delete
            ),
        path(
            f'{FILE_METADATA_NAME}/ModelMetadataWriter/filter_by_application',
            ModelMetadataWriter.filter_by_application
            )
]
