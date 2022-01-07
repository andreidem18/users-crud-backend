from rest_framework.serializers import ModelSerializer, JSONField
from occupations.models import Occupation
from drf_yasg import openapi
from occupations.serializer import OccupationSerializer
from .models import User
        

class UserSerializer(ModelSerializer):
    occupation = OccupationSerializer(read_only=True)
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'birthday', 'occupation')
        
class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'first_name', 'last_name', 'birthday', 'occupation')
        