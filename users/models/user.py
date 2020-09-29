from django.contrib.auth.models import AbstractUser
from django.db import models, transaction

from datetime import datetime


class User(AbstractUser):
    last_action = models.DateTimeField(verbose_name='Last action datetime', null=True, blank=True)

    def update_last_action(self):
        self.last_action = datetime.now()
        self.save()

class UserManager(models.Manager):
    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('username needed')
        try:
            with transaction.atomic():
                user = self.model(username=username, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise

    def create_user(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, password, **extra_fields)