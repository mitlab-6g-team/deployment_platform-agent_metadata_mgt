from django.views.decorators.http import require_POST
from main.utils.logger import log_trigger
from main.apps.file_metadata.services import common_action
from main.apps.file_metadata.models.model import Model
from main.apps.file_metadata.serializers.model import ModelWriteSerializer, ModelReadSerializer

@log_trigger("INFO")
@require_POST
def create(request):
    json_response = common_action.create(
                    request,
                    ModelWriteSerializer,
                    ModelReadSerializer
                    )

    return json_response

@log_trigger("INFO")
@require_POST
def retrieve(request):
    json_response = common_action.retrieve(
                    request,
                    Model,
                    ModelReadSerializer
                    )

    return json_response

@log_trigger("INFO")
@require_POST
def update(request):
    json_response = common_action.update(
                    request,
                    Model,
                    ModelWriteSerializer,
                    ModelReadSerializer
                    )

    return json_response

@log_trigger("INFO")
@require_POST
def delete(request):
    json_response = common_action.delete(
                    request,
                    Model
                    )

    return json_response


@log_trigger("INFO")
@require_POST
def filter_by_application(request):
    json_response = common_action.filter(
                    request,
                    Model,
                    ModelReadSerializer,
                    'application'
                    )

    return json_response
