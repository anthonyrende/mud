from django.db import models

# Create your models here.
class Room(models.Model):
    title = models.CharField(max_length=50, default='DEFAULT TITLE')
    description = models.CharField(max_length=500, default='DEFAULT DESCRIPTION')
    n_to = models.IntegerField(default=0)
    s_to = models.IntegerField(default=0)
    e_to = models.IntegerField(default=0)
    w_to = models.IntegerField(default=0)
    #TODO implement x,y int fields?