from rest_framework.viewsets import ModelViewSet
from users.serializer import UserSerializer
from .models import User

class UserViewSet(ModelViewSet):
    queryset= User.objects.all()
    serializer_class = UserSerializer
