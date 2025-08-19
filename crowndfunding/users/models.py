from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.

class CustomUser(AbstractUser):
    """
    Custom user model that extends the default Django user model.
    This can be used to add additional fields or methods specific to the application.
    """

    def __str__(self): # __str__ method to return the username / # self means the instance of the class(it's calling its own code)
        return self.username
    
    
    