from django.db import models


class Game(models.Model):
    date = models.DateField('Дата события')
    task = models.TextField('Описание события')

