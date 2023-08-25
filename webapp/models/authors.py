from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=200,
                                  verbose_name='Имя автора')
    last_name = models.CharField(max_length=200,
                                 verbose_name='Фамилия автора')

    class Meta:
        app_label = "webapp"
        verbose_name = 'Автор книги'
        verbose_name_plural = 'Авторы книг'
