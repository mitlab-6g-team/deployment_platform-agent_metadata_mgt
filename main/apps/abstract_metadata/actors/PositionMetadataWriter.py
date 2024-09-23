from django.views.decorators.http import require_POST
from main.utils.logger import log_trigger
from main.apps.abstract_metadata.services import common_action
from main.apps.abstract_metadata.models.position import Position
from main.apps.abstract_metadata.serializers.position import PositionWriteSerializer, PositionReadSerializer

@log_trigger("INFO")
@require_POST
def create(request):
    json_response = common_action.create(
                    request,
                    PositionWriteSerializer,
                    PositionReadSerializer
                    )

    return json_response

@log_trigger("INFO")
@require_POST
def retrieve(request):
    json_response = common_action.retrieve(
                    request,
                    Position,
                    PositionReadSerializer
                    )

    return json_response

@log_trigger("INFO")
@require_POST
def update(request):
    json_response = common_action.update(
                    request,
                    Position,
                    PositionWriteSerializer,
                    PositionReadSerializer
                    )

    return json_response

@log_trigger("INFO")
@require_POST
def delete(request):
    json_response = common_action.delete(
                    request,
                    Position
                    )

    return json_response


@log_trigger("INFO")
@require_POST
def filter_by_application(request):
    json_response = common_action.filter(
                    request,
                    Position,
                    PositionReadSerializer,
                    'application'
                    )

    return json_response
