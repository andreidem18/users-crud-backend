from django.db import models
from occupations.models import Occupation
from django.contrib.auth.models import AbstractUser, BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, username=None, **extra_fields):
        if not email:
            raise ValueError('Users must have a valid email')
        user = self.model(
            email = self.normalize_email(email),
            password=password,
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password, username=None, **extra_fields):
        user = self.create_user(
            email = email,
            password=password,
            username=username,
            **extra_fields
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, username=None, **extra_fields):
        user = self.create_user(
            email=email, password=password, username=username,
            **extra_fields
        )
        user.is_staff = True
        user.is_admin = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    email = models.EmailField(max_length=150, unique=True, null=False)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    birthday = models.DateField(blank=True, null=True)
    occupation = models.ForeignKey(
        Occupation,
        on_delete=models.SET_NULL,
        null=True
    )
    username = models.CharField(max_length=10, unique=False, default='', blank=True, null=True)


    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email
