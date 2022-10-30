"""This module defines urls of chats app"""
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Chat


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def default_chat_handler(request):
    """This view shows all chats or adds a new chat"""

    if request.method == 'GET':
        try:
            chats = Chat.objects.all()

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
        except Chat.DoesNotExist:
            return JsonResponse(
                {
                    'title': 'No objects found',
                    'detail': 'Query to get objects from chats_chat failed'
                },
                status=400
            )
    else:
        title = request.POST.get('Title', None)

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
@require_http_methods(['GET', 'PUT', 'DELETE'])
def rud_chat_handler(request, chat_id):
    """This view shows, updates, deletes a chat with id==chat_id"""

    try:
        chat = Chat.objects.get(id=chat_id)

        if request.method == 'GET':
            return JsonResponse(
                {
                    'id': chat.id,
                    'title': chat.title,
                    'datetime_created': chat.datetime_created
                }
            )
        elif request.method == 'PUT':
            request.method = 'POST'
            title = request.POST.get('Title', None)
            request.method = 'PUT'

            if title:
                chat = Chat.objects.get(id=chat_id)
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
        else:
            chat.delete()

            return HttpResponse(status=204)
    except Chat.DoesNotExist:
        return JsonResponse(
            {
                'title': 'No objects found',
                'detail': 'Query to get object from chats_chat by id failed'
            },
            status=400
        )
