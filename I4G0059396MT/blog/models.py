from argparse import OPTIONAL
from doctest import OPTIONFLAGS_BY_NAME
from turtle import title
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Fields(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank = True)
    author = get_user_model()
    created_date = models.DateTimeField(OPTIONAL)
    published_date = models.DateTimeField(OPTIONFLAGS_BY_NAME)
