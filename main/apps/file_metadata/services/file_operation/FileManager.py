"""
This module provides APIs that topic_operation needs to call.
"""
from main.utils import request
from main.utils.config import config

def check(payload):
    """
    Call file_operation.FileManager.check API
    """
    module_name_str = config.FILE_OPERATION.NAME
    actor_name_str = "FileManager"
    function_name_str = "check"

    response = request.for_json(module_name_str, actor_name_str, function_name_str, payload)

    response_dict = response.json()
    response_dict = response_dict["data"]

    return response_dict

def remove(payload):
    """
    Call file_operation.FileManager.remove API
    """
    module_name_str = config.FILE_OPERATION.NAME
    actor_name_str = "FileManager"
    function_name_str = "remove"

    response = request.for_json(module_name_str, actor_name_str, function_name_str, payload)

    response_dict = response.json()
    response_dict = response_dict["detail"]

    return response_dict