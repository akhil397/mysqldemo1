from django.db import models
# user = appone pass = one123

# Create your models here.
class VideoData(models.Model):
  title = models.CharField(max_length=255)
  link = models.CharField(max_length=255)
  images = models.ImageField(upload_to="images")
  
def __str__(self):
         return '{}'.format(self.title)
