from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User
from rest_framework import permissions
from .serializers import RegisterSerializer,UserSerializer,CustomTokenObtainPairSerializer
# Create your views here.


class Register(APIView):
    def post(self,request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        user = serializer.create(serializer.validated_data)
        refresh = RefreshToken.for_user(user)
        user = UserSerializer(user)
        data = {
            "refresh":str(refresh),
            "access":str(refresh.access_token),
            "user":user.data
        }
        return Response(data,status=status.HTTP_201_CREATED)


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class VerifyUser(APIView):
    permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = (TokenAuthentication,)

    def get(self,request):
        user = request.user
        print("######################################",user.id)
        user = UserSerializer(user)
        data = {"user":user.data}
        print("############3444444444444444",data)
        return Response(data,status=status.HTTP_200_OK)