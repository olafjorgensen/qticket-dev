from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Add any addition fields here.
    username = None
    email = models.EmailField(unique=True)
    reg_date = models.DateTimeField(auto_now_add=True)

   
