from django.db import models
from datetime import datetime
from django.contrib.auth.models import User



class GameManger(models.Manager):
    def create_game(self, name):
        game = self.create(name=name, date=datetime.now().date(), task="bla bla")
        # do something with the book
        return game


class Game(models.Model):
    name = models.CharField('Имя события', max_length=50)
    task = models.TextField('Описание события')
    date = models.DateField('Дата события')

    objects = GameManger()
    def __str__(self):
        return self.name, self.task, self.date

