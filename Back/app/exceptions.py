# app/exceptions.py
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    
    if response is not None and response.status_code == 403:
        response.data['detail'] = "Não tem permissão para fazer login como professor🤚"
        
    if response is not None and response.status_code == 401:
        response.data['detail'] = "Não possui autorização🚫"
        response.data['code'] = "Token invalido"

    return response
