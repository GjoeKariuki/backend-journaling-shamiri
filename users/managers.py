from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _



class CustomUserManager(BaseUserManager):
    """ custom user model where email is the unique identifier for authentication"""
    def create_user(self,email,password,**extra_fields):
        """create and save user """
        if not email:
            raise(_(ValueError("The email must be set")))
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)        
        user.set_password(password)
        user.save()

        return user