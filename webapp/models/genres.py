from django.db import models


class Genre(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name='Жанр книги')

    class Meta:
        app_label = "webapp"
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
