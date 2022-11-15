"""This module defines views of users app"""

from django.http import JsonResponse, HttpResponse, QueryDict
from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import User


@csrf_exempt
@require_http_methods(['GET'])
def get_users(request):
    """This view shows all users"""

    users = get_list_or_404(User)

    user_list = []
    for obj in users:
        user_list.append(
            {
                'id': obj.id,
                'phone_number': obj.phone_number,
                'username': obj.username
            }
        )

    return JsonResponse({'users': user_list})


@csrf_exempt
@require_http_methods(['POST'])
def add_user(request):
    """This view adds a new user"""

    phone_number = request.POST.get('phone_number')
    username = request.POST.get('username')

    if phone_number and username:
        is_exist = User.objects.get(username=username)
        if is_exist is None:
            user = User.objects.create(
                phone_number=phone_number,
                username=username
            )

            return JsonResponse(
                {
                    'id': user.id,
                    'phone_number': user.phone_number,
                    'username': user.username
                },
                status=201
            )
        return HttpResponse(status=409)

    return JsonResponse(
        {
            'title': 'Expected payload',
            'detail': 'No keyword "phone_number" or "username"'
        },
        status=400
    )


@csrf_exempt
@require_http_methods(['GET'])
def get_user(request, user_id):
    """This view shows a user with id==user_id"""

    user = get_object_or_404(User, id=user_id)

    return JsonResponse(
        {
            'id': user.id,
            'phone_number': user.phone_number,
            'username': user.username
        }
    )


@csrf_exempt
@require_http_methods(['PUT'])
def update_user(request, user_id):
    """This view updates a user with id==user_id"""

    user = get_object_or_404(User, id=user_id)

    put = QueryDict(request.body)
    phone_number = put.get('phone_number')
    username = put.get('username')

    if phone_number and username:
        user.phone_number = phone_number
        user.username = username
        user.save()

        return JsonResponse(
            {
                'id': user.id,
                'phone_number': user.phone_number,
                'username': user.username
            },
            status=200
        )

    return JsonResponse(
        {
            'title': 'Expected payload',
            'detail': 'No keyword "phone_number" or "username"'
        },
        status=400
    )


@csrf_exempt
@require_http_methods(['DELETE'])
def delete_user(request, user_id):
    """This view deletes a user with id==user_id"""

    user = get_object_or_404(User, id=user_id)
    user.delete()

    return HttpResponse(status=204)
