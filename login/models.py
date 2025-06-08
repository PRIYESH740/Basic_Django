from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import validate_email

class CustomUser(AbstractUser):
    # Make email unique but keep username non-unique
    email = models.EmailField(
        unique=True,
        validators=[validate_email],
        error_messages={
            'unique': "This email is already registered.",
        }
    )
    
    # Remove username uniqueness constraint
    username = models.CharField(
        max_length=150,
        unique=False,  # This allows duplicate usernames
        help_text='150 characters or fewer. Letters, digits and @/./+/-/_ only.',
    )

    USERNAME_FIELD = 'email'  # Use email as the login identifier
    REQUIRED_FIELDS = ['username']  # Fields required when creating superuser

    def __str__(self):
        return self.email