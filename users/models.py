from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='E-Mail')

    phone = models.CharField(max_length=35, verbose_name='Phone', **NULLABLE)
    telegram = models.CharField(max_length=150, verbose_name='Telegram Username', **NULLABLE)
    city =  models.CharField(max_length=150, verbose_name='City', **NULLABLE)

    avatar = models.ImageField(upload_to='users/', verbose_name='Avatar', **NULLABLE)
    is_active = models.BooleanField(default=False, verbose_name='activity')



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.username} ({self.telegram})'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'