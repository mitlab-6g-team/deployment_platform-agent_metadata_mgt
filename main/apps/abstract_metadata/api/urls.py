from django.urls import path
from main.utils.config import config
from main.apps.abstract_metadata.actors import ApplicationMetadataWriter
from main.apps.abstract_metadata.actors import PositionMetadataWriter
from main.apps.abstract_metadata.actors import TopicMetadataWriter

ABSTRACT_METADATA_NAME=config.ABSTRACT_METADATA.NAME

urlpatterns = [
        path(
            f'{ABSTRACT_METADATA_NAME}/ApplicationMetadataWriter/create',
            ApplicationMetadataWriter.create
            ),
        path(
            f'{ABSTRACT_METADATA_NAME}/ApplicationMetadataWriter/update',
            ApplicationMetadataWriter.update
            ),
        path(
            f'{ABSTRACT_METADATA_NAME}/ApplicationMetadataWriter/delete',
            ApplicationMetadataWriter.delete
            ),
        path(
            f'{ABSTRACT_METADATA_NAME}/ApplicationMetadataWriter/filter_by_agent',
            ApplicationMetadataWriter.filter_by_agent
            ),
        path(
            f'{ABSTRACT_METADATA_NAME}/PositionMetadataWriter/create',
            PositionMetadataWriter.create
            ),
        path(
            f'{ABSTRACT_METADATA_NAME}/PositionMetadataWriter/retrieve',
            PositionMetadataWriter.retrieve
            ),
        path(
            f'{ABSTRACT_METADATA_NAME}/PositionMetadataWriter/update',
            PositionMetadataWriter.update
            ),
        path(
            f'{ABSTRACT_METADATA_NAME}/PositionMetadataWriter/delete',
            PositionMetadataWriter.delete
            ),
        path(
            f'{ABSTRACT_METADATA_NAME}/PositionMetadataWriter/filter_by_application',
            PositionMetadataWriter.filter_by_application
            ),
        path(
            f'{ABSTRACT_METADATA_NAME}/TopicMetadataWriter/create',
            TopicMetadataWriter.create
            ),
        path(
            f'{ABSTRACT_METADATA_NAME}/TopicMetadataWriter/retrieve',
            TopicMetadataWriter.retrieve
            ),
        path(
            f'{ABSTRACT_METADATA_NAME}/TopicMetadataWriter/delete',
            TopicMetadataWriter.delete
            ),
        path(
            f'{ABSTRACT_METADATA_NAME}/TopicMetadataWriter/filter_by_agent',
            TopicMetadataWriter.filter_by_agent
            ),
]
