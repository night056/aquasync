"""
from django.db import models
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import check_password

class Owner(models.Model):
    owner_name = models.CharField(max_length=255)
    owner_phone = models.CharField(max_length=15)
    owner_email = models.EmailField()
    owner_address = models.TextField()
    license_no = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    registration_date = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)
    
class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    password = models.CharField(max_length=255)
    registration_date = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
"""
from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
from django.db import models
from django.utils.translation import gettext as _
# Create your models here.
#from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('Customer', 'Customer'),
        ('Owner', 'Boat Owner'),
        ('Administrator', 'Administrator'),
        ('Authority', 'Government authorities')
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to.'),
        related_name='customuser_groups'  # Use a different related_name
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='customuser_user_permissions'  # Use a different related_name
    )

    def _str_(self):
        return self.username

class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    age = models.PositiveIntegerField(default=18)
    email = models.EmailField(unique=True)

    def _str_(self):
        return f'Customer: {self.user.username}'

class Owner(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    license = models.CharField(max_length=100, unique=True, default="1234")
    
    def _str_(self):
        return f'Owner: {self.user.username}'

class Administrator(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    admin_id = models.CharField(max_length=20, unique=True)
    def _str_(self):
        return f'Administrator: {self.user.username}, Admin ID: {self.admin_id}'
    
class Authority(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    auth_id = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True, default='lolol')
    def _str_(self):
        return f'Authrity: {self.user.username}, Auth ID: {self.auth_id}'