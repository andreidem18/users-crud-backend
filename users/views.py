from rest_framework.viewsets import ModelViewSet

from users.serializer import CreateUserSerializer, UserSerializer
from .models import User

class UserViewSet(ModelViewSet):
    queryset= User.objects.all()
    serializer_class = UserSerializer
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateUserSerializer
        return super().get_serializer_class()
