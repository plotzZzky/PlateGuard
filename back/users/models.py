from django.db import models

from django.contrib.auth.models import User
from plates.models import ListPlates


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    office = models.ForeignKey(ListPlates, on_delete=models.CASCADE, null=True, blank=True)
