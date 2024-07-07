from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from users.managers import CustomUserManager
import uuid




# Create your models here.
class CustomUser(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = ["-date_joined"]

    def __str__(self):
        return self.email


