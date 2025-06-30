from django.urls import resolve

def es_inicio_context(request):
    return {
        'es_inicio': resolve(request.path_info).url_name == 'inicio'
    }