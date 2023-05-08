from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


from .models import Profile
from .validate import valid_user
from plates.models import ListPlates
from .serializer import serialize_offices


@api_view(['POST'])
@csrf_exempt
def register_user(request):
    try:
        password = request.data['password1']
        pwd = request.data['password2']
        username = request.data['username']
        email = request.data['email']
        post_name = request.data['office']
        if valid_user(password, pwd, username, email):
            user = User(username=username, email=email, password=password)
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password)
            token = Token.objects.create(user=user)  # type:ignore
            try:
                if post_name == '':
                    return JsonResponse({"error": "Informações faltando!"}, status=300)
                lp = ListPlates.objects.get(name=post_name)  # type:ignore
            except ListPlates.DoesNotExist:  # type:ignore
                lp = ListPlates(name=post_name)
                lp.save()
            profile = Profile(user=user, office=lp)
            profile.save()
            return JsonResponse({"token": token.key}, status=200)
        else:
            return JsonResponse({"error": "Informações incorretas!"}, status=300)
    except KeyError:
        return JsonResponse({"error": "Informações faltando!"}, status=300)


@api_view(['POST'])
@csrf_exempt
def login(request):
    try:
        password = request.data['password']
        username = request.data['username']
        user = authenticate(username=username, password=password)
        if user is not None:
            token = Token.objects.get(user=user)  # type:ignore
            return JsonResponse({"token": token.key}, status=200)
        else:
            return JsonResponse({"error": "Login incorreto!"}, status=300)
    except KeyError:
        return JsonResponse({"error": "Login incorreto!"}, status=404)


@api_view(['GET'])
def get_offices(request):
    offices = ListPlates.objects.all()  # type: ignore
    data = [serialize_offices(item) for item in offices]
    return JsonResponse({"offices": data}, status=200)
