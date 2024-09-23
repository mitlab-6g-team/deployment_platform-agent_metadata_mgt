from django.db.models.signals import post_delete
from django.dispatch import receiver
from main.apps.file_metadata.models.model import Model
from main.apps.file_metadata.services.file_operation import FileManager


@receiver(post_delete, sender=Model)
def delete_model_from_minio(sender, instance, **kwargs):
    
    model_uid_str = instance.uid
    model_uid_str = str(model_uid_str)
    source_uid_str = str(instance.source)
    file_extension_str = str(instance.file_extension)

    folder_path_str = "inference_file_system/"
    file_name_str = model_uid_str

    if source_uid_str is None:
        folder_path_str = folder_path_str + model_uid_str
    else:
        folder_path_str = source_uid_str

    model_file_path_str = folder_path_str + '/' + file_name_str + file_extension_str
    payload_dict = {"file_path": model_file_path_str}
    model_exist_bol = FileManager.check(payload_dict)
    print(model_exist_bol)

    if model_exist_bol:
        payload_dict = {"file_path": model_file_path_str}
        FileManager.remove(payload_dict)

    tmeplate_folder_path_str = folder_path_str + '/' +  'template'
    payload_dict = {"file_path": tmeplate_folder_path_str}
    template_exist_bol = FileManager.check(payload_dict)

    if template_exist_bol:
        payload_dict = {"file_path": tmeplate_folder_path_str}
        FileManager.remove(payload_dict)
