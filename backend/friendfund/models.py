from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):

    mondo_id = models.CharField(max_length=255)
    user = models.OneToOneField(User)
