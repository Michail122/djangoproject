from django.db import models

class Game(models.Model):
    data= models.CharField('Дата события', max_length=50)
    task= models.TextField('Описание события')
# Create your models here.
