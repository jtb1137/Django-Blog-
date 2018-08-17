from django.db import models
from datetime import datetime, timezone, timedelta

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=100)
  body = models.TextField()
  pub_date = models.DateTimeField('date published')

  def __str__(self):
    return self.title
  
  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)