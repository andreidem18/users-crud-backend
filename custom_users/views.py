from custom_users.serializer import CreateUserSerializer
from custom_users.serializer import UserSerializer
from main.get_client_ip import get_client_ip
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser

class UserViewSet(ModelViewSet):
    queryset= CustomUser.objects.all()
    serializer_class = UserSerializer

    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(created_by=get_client_ip(request))
        serialized = UserSerializer(queryset, many=True)
        return Response(serialized.data)

    def create(self, request, *args, **kwargs):
        request.data['created_by']=get_client_ip(request)
        serialized = CreateUserSerializer(data=request.data)
        if not serialized.is_valid():
            return Response(status = status.HTTP_400_BAD_REQUEST, data = serialized.errors)
        else:
            serialized.save()
            serialized = UserSerializer(serialized.data)
            return Response(status = status.HTTP_201_CREATED, data = serialized.data)
            