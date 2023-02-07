from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from ..serializers import RegisterSerializer

from drf_yasg.utils import swagger_auto_schema

def serialize_user(user):
    return {
        "username": user.username,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name
    }

@swagger_auto_schema(
    method='post', 
    request_body=RegisterSerializer,
    operation_summary="Register a user",
    operation_description="Type correct form and receive a account user",
    responses={200: 'successful registration'})
@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        _, token = AuthToken.objects.create(user)
        return Response({
            "user_info": serialize_user(user),
            "token": token
        })

@swagger_auto_schema(
    method='post', 
    request_body=AuthTokenSerializer,
    operation_summary="Login user",
    operation_description="Type correct username and password",
    responses={200: 'successful registration'})
@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user)
    return Response({
        'user_data': serialize_user(user),
        'token': token
    })


        





