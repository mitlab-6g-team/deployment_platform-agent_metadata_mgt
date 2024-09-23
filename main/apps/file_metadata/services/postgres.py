from django.shortcuts import get_object_or_404

def create(write_serializer, read_serializer, data_dict):
    serializer = write_serializer(data=data_dict)
    if serializer.is_valid():
        model_instance = serializer.save()
        metadata_dict = read_serializer(model_instance).data
        return metadata_dict

def retrieve(model, read_serializer, data_dict):
    uid_str = data_dict['uid']
    model_instance = get_object_or_404(model, **{'uid': uid_str})
    serializer = read_serializer(model_instance)
    metadata_dict = serializer.data
    return metadata_dict

def update(model, write_serializer, read_serializer, data_dict):
    uid_str = data_dict['uid']
    model_instance = get_object_or_404(model, **{'uid': uid_str})
    serializer = write_serializer(model_instance, data=data_dict, partial=True)
    if serializer.is_valid():
        model_instance = serializer.save()
        metadata_dict = read_serializer(model_instance).data
        return metadata_dict

def delete(model, data_dict):
    uid_str = data_dict['uid']
    model_instance = get_object_or_404(model, **{'uid': uid_str})
    model_instance.delete()

def filter(model, read_serializer, data_dict, type_str):

    foreign_key_str = f'f_{type_str}_uid'
    foreign_key_dict = {foreign_key_str: data_dict['uid']}

    models_instance = model.objects.filter(**foreign_key_dict)
    serializer = read_serializer(models_instance, many=True)
    metadata_dict = serializer.data
    return metadata_dict
