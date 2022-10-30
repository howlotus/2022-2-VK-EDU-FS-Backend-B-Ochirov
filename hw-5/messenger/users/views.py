"""This module defines urls of users app"""

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import User


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def default_user_handler(request):
    """This view shows all users or adds a new user"""

    if request.method == 'GET':
        try:
            users = User.objects.all()

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
        except User.DoesNotExist:
            return JsonResponse(
                {
                    'title': 'No objects found',
                    'detail': 'Query to get objects from users_user failed'
                },
                status=400
            )
    else:
        phone_number = request.POST.get('phone_number', None)
        username = request.POST.get('username', None)

        if phone_number and username:
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

        return JsonResponse(
            {
                'title': 'Expected payload',
                'detail': 'No keyword "phone_number" or "username"'
            },
            status=400
        )


@csrf_exempt
@require_http_methods(['GET', 'PUT', 'DELETE'])
def rud_user_handler(request, user_id):
    """This view shows, updates, deletes a user with id==user"""

    try:
        user = User.objects.get(id=user_id)

        if request.method == 'GET':
            return JsonResponse(
                {
                    'id': user.id,
                    'phone_number': user.phone_number,
                    'username': user.username
                }
            )
        elif request.method == 'PUT':
            request.method = 'POST'
            phone_number = request.POST.get('phone_number', None)
            username = request.POST.get('username', None)
            request.method = 'PUT'

            if phone_number and username:
                user = User.objects.get(id=user_id)
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
        else:
            user.delete()

            return HttpResponse(status=204)
    except User.DoesNotExist:
        return JsonResponse(
            {
                'title': 'No objects found',
                'detail': 'Query to get object from users_user by id failed'
            },
            status=400
        )
