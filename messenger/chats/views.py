"""This module defines views of chats app"""

from django.http import JsonResponse, HttpResponse, QueryDict
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Chat


@csrf_exempt
@require_http_methods(['GET'])
def get_chats(request):
    """This view shows all chats"""

    chats = get_list_or_404(Chat)

    chat_list = []
    for obj in chats:
        chat_list.append(
            {
                'id': obj.id,
                'title': obj.title,
                'datetime_created': obj.datetime_created
            }
        )

    return JsonResponse({'chats': chat_list})


@csrf_exempt
@require_http_methods(['POST'])
def add_chat(request):
    """This view adds a new chat"""

    title = request.POST.get('Title')

    if title:
        chat = Chat.objects.create(title=title)

        return JsonResponse(
            {
                'id': chat.id,
                'title': chat.title,
                'datetime_created': chat.datetime_created
            },
            status=201
        )

    return JsonResponse(
        {
            'title': 'Expected payload',
            'detail': 'No keyword "Title"'
        },
        status=400
    )


@csrf_exempt
@require_http_methods(['GET'])
def get_chat(request, chat_id):
    """This view shows a chat with id==chat_id"""

    chat = get_object_or_404(Chat, id=chat_id)

    return JsonResponse(
        {
            'id': chat.id,
            'title': chat.title,
            'datetime_created': chat.datetime_created
        }
    )


@csrf_exempt
@require_http_methods(['PUT'])
def update_chat(request, chat_id):
    """This view updates a user with id==chat_id"""

    chat = get_object_or_404(Chat, id=chat_id)

    put = QueryDict(request.body)
    title = put.get('title')

    if title:
        chat.title = title
        chat.save()

        return JsonResponse(
            {
                'id': chat.id,
                'title': chat.title,
                'datetime_created': chat.datetime_created
            },
            status=200
        )

    return JsonResponse(
        {
            'title': 'Expected payload',
            'detail': 'No keyword "Title"'
        },
        status=400
    )


@csrf_exempt
@require_http_methods(['DELETE'])
def delete_chat(request, chat_id):
    """This view deletes a user with id==chat_id"""

    chat = get_object_or_404(Chat, id=chat_id)
    chat.delete()

    return HttpResponse(status=204)
