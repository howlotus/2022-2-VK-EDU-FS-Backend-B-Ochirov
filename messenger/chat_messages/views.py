"""This module defines urls of chat_messages app"""

from django.http import HttpResponse, JsonResponse, QueryDict
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Message
from chats.models import ChatMember


@csrf_exempt
@require_http_methods(['GET'])
def get_messages(request):
    """This view shows all messages of chat and/or user"""

    chat_id = request.GET.get('chat_id')
    sender_id = request.GET.get('user_id')

    context = {}
    if chat_id:
        context['chat_id'] = chat_id
    if sender_id:
        context['sender_id'] = sender_id

    messages = get_list_or_404(Message, **context)

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
        return JsonResponse({'messages': message_list})
    else:
        return HttpResponse(status=204)


@csrf_exempt
@require_http_methods(['POST'])
def add_message(request):
    """This view adds a new message in chat"""

    chat_id = request.POST.get('chat_id')
    sender_id = request.POST.get('sender_id')
    content = request.POST.get('content')
    status = request.POST.get('status')

    if chat_id and sender_id and content and status:
        chat_members = get_list_or_404(ChatMember, chat_id=chat_id)

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
@require_http_methods(['GET'])
def get_message(request, message_id):
    """This view shows a message with id==message_id"""

    message = get_object_or_404(Message, id=message_id)

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


@csrf_exempt
@require_http_methods(['PUT'])
def update_message(request, message_id):
    """This view updates a message with id==message_id"""

    message = get_object_or_404(Message, id=message_id)

    put = QueryDict(request.body)
    chat_id = put.get('chat_id')
    sender_id = put.get('sender_id')
    content = put.get('content')
    status = put.get('status')

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


@csrf_exempt
@require_http_methods(['DELETE'])
def delete_message(request, message_id):
    """This view deletes a message with id==message_id"""

    message = get_object_or_404(Message, id=message_id)
    message.delete()

    return HttpResponse(status=204)
