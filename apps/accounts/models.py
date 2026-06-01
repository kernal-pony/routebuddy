import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)

    # Enforce email and username during creation
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return f"{self.username} ({self.email})"
