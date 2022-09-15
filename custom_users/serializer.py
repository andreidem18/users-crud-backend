from rest_framework.serializers import ModelSerializer
from .models import CustomUser
        

class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'birthday')

class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'birthday', 'created_by')
