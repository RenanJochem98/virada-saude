# from datetime import datetime
# import constants

# from tkinter import CASCADE
from hashids import Hashids

from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# from django.core.exceptions import PermissionDenied
from django.db import models
# from anamnese.models import Anamnese

hashids = Hashids(min_length=3, alphabet="abcdefghijklmnopqrstuvwxyz0123456789")


class RegistrationForm(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    def encode(self) -> str:
        return hashids.encode(self.id)

    @classmethod
    def decode(cls, string: str) -> "RegistrationForm":
        return cls.objects.filter(id=hashids.decode(string)[0]).first()


class UserManager(BaseUserManager):
    use_in_migrations = True

    # def get_queryset(self):
    #     return super().get_queryset()

    # def create(self, **kwargs):
    #     return super().create(**kwargs)

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password=password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
#class User(models.Model):
    email = models.EmailField("email", blank=True, null=False)
    #username = models.CharField("username", max_length=150, blank=False, null=False)
    first_name = models.CharField("Primeiro nome", max_length=150, blank=True, null=True)
    last_name = models.CharField("Sobrenome", max_length=150, blank=True, null=True)
    
    is_active = models.BooleanField("is_active", default=True)
    is_staff = models.BooleanField("is_staff", default=False)
    is_superuser = models.BooleanField("is_superuser", default=False)

    date_joined = models.DateTimeField("date_joined", default=timezone.now)
    created = models.DateTimeField("created", default=timezone.now)
    modified = models.DateTimeField("modified", auto_now=True)
   
    empresa = models.ForeignKey(
        "empresa.Empresa",
        verbose_name="Empresa",
        related_name="idempresas",
        on_delete=models.RESTRICT,
        blank=True,
        null=True
    )

   
    
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    
    
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        constraints = [
            models.UniqueConstraint(
                fields=["email"],
                name="unique_email",
            )
        ]

    def __str__(self):
        return self.email


    # def BuscarAnamneses(self):
    #     return Anamnese.objects.get(usuario = self.id)