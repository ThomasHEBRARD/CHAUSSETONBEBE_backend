from django.db import models


class HomePageModel(models.Model):
    name = models.CharField(max_length=100, default='DefaultName')
    code = models.CharField(max_length=100, default='DefaultCode')
    title = models.CharField(max_length=250, default='DefaultTile')

    def __str__(self):
        return self.name
