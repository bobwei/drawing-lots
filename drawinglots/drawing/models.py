from django.db import models
from django.contrib.auth.models import User

from imagekit.models import ProcessedImageField
from imagekit.processors import SmartResize

# Create your models here.
class Game(models.Model):
    owner = models.ForeignKey(User)
    created_time = models.DateTimeField(auto_now_add=True)

class Item(models.Model):
    game = models.ForeignKey(Game)
    picture = ProcessedImageField(upload_to='drawing/item', 
                                  processors=[SmartResize(600, 
                                                          600)], 
                                  format='JPEG', 
                                  options={'quality': 90},
                                  height_field='picture_height', 
                                  width_field='picture_width')
    picture_height = models.PositiveIntegerField(null=True, blank=True)
    picture_width = models.PositiveIntegerField(null=True, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    number = models.PositiveIntegerField(null=True, blank=True)