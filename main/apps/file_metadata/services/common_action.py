from main.utils.packet import unpacking
from main.apps.file_metadata.services import postgres
from django.http import JsonResponse

def create(request, write_serializer, read_serializer):
    data_dict = unpacking(request, 'json')

    metadata_dict = postgres.create(write_serializer, read_serializer, data_dict)

    response_dict = {
                    "detail":"Metadata created successfully",
                    "data": metadata_dict
                    }
    return JsonResponse(response_dict, status=200)

def retrieve(request, model, read_serializer):
    data_dict = unpacking(request, 'json')

    metadata_dict = postgres.retrieve(model, read_serializer, data_dict)

    response_dict = {
                    "detail":"Metadata retrieved successfully",
                    "data": metadata_dict
                    }
    return JsonResponse(response_dict, status=200)

def update(request, model, write_serializer, read_serializer):
    data_dict = unpacking(request, 'json')
    print(data_dict)
    metadata_dict = postgres.update(model, write_serializer, read_serializer, data_dict)

    response_dict = {
                    "detail":"Metadata updated successfully",
                    "data": metadata_dict
                    }
    return JsonResponse(response_dict, status=200)

def delete(request, model):
    data_dict = unpacking(request, 'json')

    postgres.delete(model, data_dict)

    response_dict = {
                    "detail":"Metadata deleted successfully"
                    }
    return JsonResponse(response_dict, status=200)

def filter(request, model, read_serializer, type_str):

    data_dict = unpacking(request, 'json')

    metadata_list = postgres.filter(model, read_serializer, data_dict, type_str)

    response_dict = {
                    "detail":"Metadatas retrieved successfully",
                    "data": metadata_list
                    }

    return JsonResponse(response_dict, status=200)
