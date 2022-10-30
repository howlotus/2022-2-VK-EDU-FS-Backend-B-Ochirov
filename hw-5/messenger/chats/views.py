"""This module defines urls of chats app"""

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from .models import Chat


@csrf_exempt
@require_http_methods(['GET'])
def chat_menu(request):
    """This view renders a menu html page"""

    return render(request, "index.html")


@csrf_exempt
@require_http_methods(['POST'])
def create_chat_handler(request):
    """This view adds a new chat"""

    title = request.POST.get('Title', None)

    if title:
        Chat.objects.create(title=title)

        return HttpResponse(status=201)

    return JsonResponse({'Error': 'No attribute title'})


@csrf_exempt
@require_http_methods(['GET'])
def chat_list(request):
    """This view shows all chats"""

    try:
        chats = Chat.objects.all()


    except Chat.DoesNotExist:
        pass

    return HttpResponse(status=404)


@csrf_exempt
@require_http_methods(['GET', 'DELETE'])
def edit_chat_handler(request, chat_id):
    """This view shows, deletes a chat with id==chat_id"""

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
        else:
            chat.delete()

            return HttpResponse(status=204)
    except Chat.DoesNotExist:
        return JsonResponse({'Error': 'inappropriate value'})
