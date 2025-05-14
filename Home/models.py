from django.db import models
from tinymce.models import HTMLField

class News(models.Model):
    news_title=models.CharField(max_length=75)
    news_icon=models.CharField(max_length=20,blank=True,null=True)
    news_desc=HTMLField()
