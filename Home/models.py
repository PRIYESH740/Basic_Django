from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

class News(models.Model):
    news_title=models.CharField(max_length=75)
    news_icon=models.CharField(max_length=20,blank=True,null=True)
    news_desc=HTMLField()
    news_slug=AutoSlugField(populate_from='news_title',unique=True,null=True, default=None)
