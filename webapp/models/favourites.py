from django.db import models
from django.contrib.auth.models import User


class Favourites(models.Model):
    user_id = models.ForeignKey(User,
                                verbose_name='Пользователь',
                                on_delete=models.CASCADE,
                                related_name='favourites')
    book_id = models.ForeignKey('webapp.Book',
                                verbose_name='Книга',
                                on_delete=models.CASCADE,
                                related_name='favourites')

    class Meta:
        app_label = "webapp"
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'
