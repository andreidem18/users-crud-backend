from main.get_client_ip import get_client_ip
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from users.serializer import UserSerializer
from .models import User

class UserViewSet(ModelViewSet):
    queryset= User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        user = User.objects.create(
            email = request.data['email'],
            first_name = request.data['first_name'],
            last_name = request.data['last_name'],
            birthday = request.data['birthday'],
            password = request.data['password'],
            created_by=get_client_ip(request)
        )
        serialized = UserSerializer(user)
        return Response(status = status.HTTP_201_CREATED, data = serialized.data)
