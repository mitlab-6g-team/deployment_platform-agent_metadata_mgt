import json

def unpacking(request, input_type):
    """ 
        Convert http request data into json data
    """
    if input_type == 'json':
        request_body_data = request.body
        request_json_data = json.loads(request_body_data)
        return request_json_data
