from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])


def add_view(request):
    body = request.GET
    if body.get('A').isdigit() and body.get('B').isdigit():
        add_result = int(body.get('A')) + int(body.get('B'))
        return JsonResponse({'result': add_result})
    else:
        return JsonResponse({'error': 'You may have entered letters'})

def subtract_view(request):
    body = request.GET
    if body.get('A').isdigit() and body.get('B').isdigit() and int(body.get('A')) > int(body.get('B')):
        add_result = int(body.get('A')) - int(body.get('B'))
        return JsonResponse({'result': add_result})
    else:
        return JsonResponse({'error': 'Perhaps you entered letters or A is less than B. You need to enter numbers A > B'})

def multiply_view(request):
    body = request.GET
    if body.get('A').isdigit() and body.get('B').isdigit():
        add_result = int(body.get('A')) * int(body.get('B'))
        return JsonResponse({'result': add_result})
    else:
        return JsonResponse({'error': 'Perhaps you entered letters or A is less than B. You need to enter numbers A > B'})

def divide_view(request):
    body = request.GET
    if body.get('A').isdigit() and body.get('B').isdigit() and int(body.get('A')) > int(body.get('B')):
        add_result = int(body.get('A')) // int(body.get('B'))
        return JsonResponse({'result': add_result})
    else:
        return JsonResponse({'error': 'Perhaps you entered letters or A is less than B. You need to enter numbers A > B'})
