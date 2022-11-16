from django.http import JsonResponse, QueryDict, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import ChatMember
from chats.models import Chat
from users.models import User


# Create your views here.
@csrf_exempt
@require_http_methods(['POST'])
def add_member(request):
    """This view adds a new member to chat"""

    chat_id = request.POST.get('chat_id')
    user_id = request.POST.get('user_id')

    if chat_id and user_id:
        get_object_or_404(Chat, id=chat_id)
        get_object_or_404(User, id=user_id)

        existing_member = ChatMember.objects.filter(chat_id=chat_id, user_id=user_id).exists()
        if existing_member:
            return JsonResponse(
                {
                    'title': 'member exists',
                    'detail': 'Attempt to add member with same params as exists',
                },
                status=403
            )

        member = ChatMember.objects.create(
            chat_id=chat_id,
            user_id=user_id
        )

        return JsonResponse(
            {
                'id': member.id,
                'chat_id': member.chat_id,
                'user_id': member.user_id,
                'datetime_added': member.datetime_added,
            },
            status=201
        )

    return JsonResponse(
        {
            'title': 'Expected payload',
            'detail': 'No keywords "chat_id", "user_id"'
        },
        status=400
    )


@csrf_exempt
@require_http_methods(['DELETE'])
def delete_member(request):
    """This view deletes a member with chat_id=chat_id, user_id=user_id"""

    delete = QueryDict(request.body)
    chat_id = delete.get('chat_id')
    user_id = delete.get('user_id')

    member = get_object_or_404(ChatMember, chat_id=chat_id, user_id=user_id)
    member.delete()

    return HttpResponse(status=204)
