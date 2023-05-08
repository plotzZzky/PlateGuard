from django.db import models


class ListPlates(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)


class Plate(models.Model):
    post_name = models.ForeignKey(ListPlates, on_delete=models.CASCADE)
    number = models.CharField(max_length=255, null=False, blank=False)
    city = models.CharField(max_length=255, null=False, blank=False)
    model = models.CharField(max_length=255, null=False, blank=False)
    manufacturer = models.CharField(max_length=255, null=False, blank=False)
    color = models.CharField(max_length=255, null=False, blank=False)
    year = models.CharField(max_length=255, null=False, blank=False)
    qru = models.CharField(max_length=255)
