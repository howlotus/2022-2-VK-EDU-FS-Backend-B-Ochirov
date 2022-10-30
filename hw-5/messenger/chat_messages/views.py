"""This module defines urls of chat_messages app"""

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Message
from chats.models import ChatMember


# Create your views here.
@csrf_exempt
@require_http_methods(['GET', 'POST'])
def default_message_handler(request):
    """This view shows all messages or adds a new message"""

    if request.method == 'GET':
        chat_id = request.GET.get('chat_id', None)
        sender_id = request.GET.get('user_id', None)
        try:
            context = {}
            if chat_id:
                context['chat_id'] = chat_id
            if sender_id:
                context['sender_id'] = sender_id

            messages = Message.objects.filter(**context)

            message_list = []
            for obj in messages:
                message_list.append(
                    {
                        'id': obj.id,
                        'chat_id': obj.chat_id,
                        'sender_id': obj.sender_id,
                        'content': obj.content,
                        'datetime_sent': obj.datetime_sent,
                        'status': obj.status
                    }
                )

            if message_list:
                return JsonResponse({'chats': message_list})
            else:
                return HttpResponse(status=204)
        except Message.DoesNotExist:
            return JsonResponse(
                {
                    'title': 'No objects found',
                    'detail': 'Query to get objects from chat_messages_message failed'
                },
                status=400
            )
    else:
        """This view adds a new message in chat"""

        chat_id = request.POST.get('chat_id', None)
        sender_id = request.POST.get('sender_id', None)
        content = request.POST.get('content', None)
        status = request.POST.get('status', None)

        if chat_id and sender_id and content and status:
            chat_members = ChatMember.objects.filter(chat_id=chat_id)

            if not chat_members:
                return JsonResponse(
                    {
                        'title': 'Not a chat',
                        'detail': 'Attempt to send message to non-existing chat'
                    },
                    status=400
                )

            members = []

            for i in chat_members:
                members.append(str(i.user_id))

            if sender_id not in members:
                return JsonResponse(
                    {
                        'title': 'Not a member',
                        'detail': 'Attempt to send message by not a member'
                    },
                    status=400
                )

            message = Message.objects.create(
                chat_id=chat_id,
                sender_id=sender_id,
                content=content,
                status=status
            )

            return JsonResponse(
                {
                    'id': message.id,
                    'chat_id': message.chat_id,
                    'sender_id': message.sender_id,
                    'content': message.content,
                    'datetime_sent': message.datetime_sent,
                    'status': message.status
                },
                status=201
            )

        return JsonResponse(
            {
                'title': 'Expected payload',
                'detail': 'No keywords "chat_id", ...'
            },
            status=400
        )


@csrf_exempt
@require_http_methods(['GET', 'PUT', 'DELETE'])
def rud_message_handler(request, message_id):
    """This view shows, updates and deletes a message with id==message_id"""

    try:
        message = Message.objects.get(id=message_id)

        if request.method == 'GET':
            return JsonResponse(
                {
                    'id': message.id,
                    'chat_id': message.chat_id,
                    'sender_id': message.sender_id,
                    'content': message.content,
                    'datetime_sent': message.datetime_sent,
                    'status': message.status
                }
            )
        elif request.method == 'PUT':
            request.method = 'POST'
            chat_id = request.POST.get('chat_id', None)
            sender_id = request.POST.get('sender_id', None)
            content = request.POST.get('content', None)
            status = request.POST.get('status', None)
            request.method = 'PUT'

            if chat_id and sender_id and content and status:
                message.chat_id = chat_id
                message.sender_id = sender_id
                message.content = content
                message.status = status
                message.save()

                return JsonResponse(
                    {
                        'id': message.id,
                        'chat_id': message.chat_id,
                        'sender_id': message.sender_id,
                        'content': message.content,
                        'datetime_sent': message.datetime_sent,
                        'status': message.status
                    },
                    status=200
                )

            return JsonResponse(
                {
                    'title': 'Expected payload',
                    'detail': 'No keywords "chat_id", ...'
                },
                status=400
            )
        else:
            message.delete()

            return HttpResponse(status=204)
    except Message.DoesNotExist:
        return JsonResponse(
            {
                'title': 'No objects found',
                'detail': 'Query to get object from chat_messages_message by id failed'
            },
            status=400
        )
