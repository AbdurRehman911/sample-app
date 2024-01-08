from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class CustomAppUser(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(blank=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(blank=True, max_length=255)
    last_name = models.CharField(blank=True, max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Course(models.Model):
    id = models.BigAutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    instructor = models.ForeignKey(CustomAppUser, on_delete=models.CASCADE, related_name='courses')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title