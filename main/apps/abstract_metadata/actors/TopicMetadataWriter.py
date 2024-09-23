from django.views.decorators.http import require_POST
from main.utils.logger import log_trigger
from main.apps.abstract_metadata.models.topic import Topic
from main.apps.abstract_metadata.serializers.topic import TopicWriteSerializer, TopicReadSerializer
from main.apps.abstract_metadata.services import common_action
from django.http import JsonResponse
from main.utils.packet import unpacking
from django.shortcuts import get_object_or_404

@log_trigger("INFO")
@require_POST
def create(request):
    json_response = common_action.create(
                    request,
                    TopicWriteSerializer,
                    TopicReadSerializer
                    )

    return json_response

@log_trigger("INFO")
@require_POST
def retrieve(request):
    data_dict = unpacking(request, 'json')

    name_str = data_dict['name']
    type_str = data_dict['type']

    search_dict = {
        'name': name_str,
        'type': type_str
    }
    model_instance = Topic.objects.filter(**search_dict).first()
    # model_instance = get_object_or_404(Topic, **search_dict)
    serializer = TopicReadSerializer(model_instance)
    metadata_dict = serializer.data

    response_dict = {
                    "detail":"Metadata deleted successfully",
                    "data": metadata_dict
                    }
    return JsonResponse(response_dict, status=200)

@log_trigger("INFO")
@require_POST
def delete(request):
    data_dict = unpacking(request, 'json')
    print(data_dict)
    name_str = data_dict['name']
    type_str = data_dict['type']
    # model_instance = Topic.objects.filter(name=name_str).first()
    # model_instance = get_object_or_404(Topic, **{'name': name_str})
    model_instance = get_object_or_404(Topic, name=name_str, type=type_str)
    model_instance.delete()

    response_dict = {"detail":"Metadata deleted successfully"}
    return JsonResponse(response_dict, status=200)

@log_trigger("INFO")
@require_POST
def filter_by_agent(request):
    metadata_model_instance = Topic.objects.all()
    metadata_list = list(metadata_model_instance.values())

    response_dict = {
            "detail":"Metadatas retrieved successfully",
            "data": metadata_list
    }
    return JsonResponse(response_dict, status=200)
