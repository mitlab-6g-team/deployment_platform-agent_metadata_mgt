from django.views.decorators.http import require_POST
from main.utils.logger import log_trigger
from main.apps.abstract_metadata.services import common_action
from main.apps.abstract_metadata.models.application import Application
from main.apps.abstract_metadata.serializers.application import ApplicationWriteSerializer, ApplicationReadSerializer
from django.http import JsonResponse

@log_trigger("INFO")
@require_POST
def create(request):
    json_response = common_action.create(
                    request,
                    ApplicationWriteSerializer,
                    ApplicationReadSerializer
                    )

    return json_response

@log_trigger("INFO")
@require_POST
def update(request):
    json_response = common_action.update(
                    request,
                    Application,
                    ApplicationWriteSerializer,
                    ApplicationReadSerializer
                    )

    return json_response

@log_trigger("INFO")
@require_POST
def delete(request):
    json_response = common_action.delete(
                    request,
                    Application
                    )

    return json_response


@log_trigger("INFO")
@require_POST
def filter_by_agent(request):
    models_instance = Application.objects.all()
    serializer = ApplicationReadSerializer(models_instance, many=True)
    application_metadatas_list = serializer.data

    response_dict = {
                    "detail":"Metadatas retrieved successfully",
                    "data": application_metadatas_list
                    }

    return JsonResponse(response_dict, status=200)
