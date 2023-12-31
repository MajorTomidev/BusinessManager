from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.conf import settings
import jwt
from django.contrib.auth.signals import user_logged_in
from rest_framework_jwt.utils import jwt_payload_handler
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.


class CreateUserAPIView(APIView):
    # Allow any user (authenticated or not) to access this url 
    permission_classes = (AllowAny,)

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = {}
        data['Response'] = 'User created successfully'
        data['Email'] = user.email
        data['Username'] = user.username
        data['status_code'] = status.HTTP_201_CREATED

        return Response(data=data, status=status.HTTP_201_CREATED)
    

@api_view(['POST'])
@permission_classes([AllowAny, ])
def authenticate_user(request):
    try:
        serializer = UserSerializer(request.user)
        email = serializer.data.get('email')
        print(email)
        username = serializer.data.get('username')

        user = User.objects.get(email=email, username=username)
        if user:
            try:
                payload = jwt_payload_handler(user)
                token = jwt.encode(payload, settings.SECRET_KEY)
                user_details = {}
                user_details['name'] = user.username
                user_details['token'] = token
                user_logged_in.send(sender=user.__class__,
                                    request=request, user=user)
                return Response(user_details, status=status.HTTP_200_OK)
            except Exception as e:
                raise e
        else:
            res = {
                'error': 'can not authenticate with the given credentials or the account has been deactivated'}
            return Response(res, status=status.HTTP_403_FORBIDDEN)
    except KeyError:
        res = {'error': 'please provide an email and a password'}
        return Response(res)

   
class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    # Allows only authenticated users to access this url
    permission_classes= (IsAuthenticated,)
    serializer_class = UserSerializer


    def get(self, request, *args, **kwargs):
        # Serializer to handle turning our User object into something that can be JSONified and sent to the client
        serializer= self.serializer_class(request.user)
        print(serializer.data)
        email = serializer.data['email']
        username = serializer.data ['username']

        if User.objects.get(username=username):
            print('Nice work')
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put (self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})
        serializer = UserSerializer(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    







