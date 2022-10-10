from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

chats = [
    {'id': 1, 'user_1': 'Sergey', 'user_2': 'Ivan'}
]


@csrf_exempt
@require_http_methods(['POST'])
def add_chat(request):
    chat_id = request.POST.get('id', None)
    user_1 = request.POST.get('user_1', None)
    user_2 = request.POST.get('user_2', None)

    if chat_id and user_1 and user_2:
        chats.append({'id': int(chat_id), 'user_1': user_1, 'user_2': user_2})

        return HttpResponse(status=201)

    return JsonResponse({'Error': 'No attribute id, user_1 or user_2'})


@csrf_exempt
@require_http_methods(['GET'])
def chat_list(request):
    return JsonResponse({'chats': chats})


@csrf_exempt
@require_http_methods(['GET'])
def chat_detail(request, chat_id):
    for chat in chats:
        if chat['id'] == chat_id:
            return JsonResponse(chat)
    return JsonResponse({'Error': 'inappropriate value'})
