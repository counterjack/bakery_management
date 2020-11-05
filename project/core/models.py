from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class DateCreatedUpdatedTimeMixin(models.Model):
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True



class UserCreatedUpdateMixing(models.Model):

    class Meta:
        abstract = True