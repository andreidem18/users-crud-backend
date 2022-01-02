from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from occupations.models import Occupation
from phones.models import Phone

from users.serializer import UserSerializer
from .models import User

class UserViewSet(ModelViewSet):
    queryset= User.objects.all()
    serializer_class = UserSerializer
    
    
    def create(self, request, *args, **kwargs):
        user = User.objects.create(
            email = request.data['email'], first_name = request.data['first_name'], last_name = request.data['last_name'], birthday = request.data['birthday'], password = request.data['password'], occupation = Occupation.objects.get(id = request.data['occupation'])
        )
        phones = list()
        for p in request.data['phones']:
            phone = Phone.objects.create(
                phone = p['phone'],
                type = p['type']
            )
            phones.append(phone)
        user.phones.set(phones)
        user.save()
        serialized = UserSerializer(user)
        return Response(status = status.HTTP_201_CREATED, data = serialized.data)
        
        
    def destroy(self, request, *args, **kwargs):
        user = User.objects.get(id = kwargs['pk'])
        for phone in user.phones.all():
            phone.delete()
        return super().destroy(request, *args, **kwargs)
        
    
