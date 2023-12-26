# your_app_name/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Owner, Customer, CustomUser, Administrator, Authority
from .serializers import OwnerSerializer, CustomerSerializer, CustomUserSerializer, AdministratorSerializer, LoginSerializer, AuthoritySerializer
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password

class CustomUserViewSet(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def perform_create(self, serializer):
        # Hash the password before saving the user
        serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
        serializer.save()

class CustomerViewSet(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OwnerViewSet(generics.ListCreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class AdministratorViewSet(generics.ListCreateAPIView):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer

class AuthorityViewSet(generics.ListCreateAPIView):
    queryset = Authority.objects.all()
    serializer_class = AuthoritySerializer

class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )

        if user:
            # Check if a token already exists for the user
            token, created = Token.objects.get_or_create(user=user)
            #return Response({'token': token.key})
            if user.role == 'Customer':
                return Response({'token': token.key, 'user_type': 'customer'})
            elif user.role == 'Owner':
                return Response({'token': token.key, 'user_type': 'owner'})
            elif user.role == 'Authority':
                return Response({'token': token.key, 'user_type': 'authority'})
            elif user.role == 'Admin':
                return Response({'token': token.key, 'user_type': 'admin'})
            else:
                return Response({'token': token.key, 'user_type': 'unknown'})
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)