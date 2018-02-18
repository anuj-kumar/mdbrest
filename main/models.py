# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=50)
    rating = models.CharField(max_length=30)
    cast = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    adult = models.BooleanField(default=False)
    year = models.IntegerField()
