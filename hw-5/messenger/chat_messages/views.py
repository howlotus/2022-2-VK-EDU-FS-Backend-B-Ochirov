"""This module defines urls of chat_messages app"""

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Message


# Create your views here.
@csrf_exempt
@require_http_methods(['POST'])
def create_message_handler(request, chat_id):
    """This view adds a new message in chat"""

    if chat_id:
        Message.objects.create(chat_id=chat_id, sender_id=None, content="Hello", status='DE')

        return HttpResponse(status=201)

    return JsonResponse({'Error': 'No attribute title'})


@csrf_exempt
@require_http_methods(['GET', 'PUT', 'DELETE'])
def edit_message_handler(request, message_id):
    """This view shows, deletes a message with id==message_id"""

    try:
        message = Message.objects.get(id=message_id)

        if request.method == 'GET':
            return JsonResponse(
                {
                    'id': message.id,
                    'content': message.content,
                    'datetime_sent': message.datetime_sent,
                    'status': message.status,
                    'chat_id': message.chat_id,
                    'sender_id': message.sender_id
                }
            )
        elif request.method == 'PUT':
            message.content = 'qqqqq'
            message.status = 'RE'
            message.save()

            return HttpResponse(status=200)
        else:
            message.delete()

            return HttpResponse(status=204)
    except Message.DoesNotExist:
        return JsonResponse({'Error': 'inappropriate value'})
