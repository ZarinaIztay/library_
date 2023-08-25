from django.db import models
from django.utils import timezone


class Book(models.Model):
    title = models.CharField(max_length=200,
                             verbose_name='Название книги')
    description = models.TextField(max_length=3000,
                                   null=False,
                                   blank=False,
                                   verbose_name='Описание книги')
    author_id = models.ForeignKey('webapp.Author',
                                  verbose_name='Автор книги',
                                  on_delete=models.CASCADE,
                                  default=1,
                                  related_name='books',)
    genre_id = models.ForeignKey('webapp.Genre',
                                 related_name='books',
                                 on_delete=models.CASCADE,
                                 verbose_name='Жанр книги'
                                 )
    publication_date = models.DateField(verbose_name='Дата публикации')

    deleted_at = models.DateTimeField(verbose_name='Дата удаления',
                                      null=True,
                                      default=None)

    is_deleted = models.BooleanField(verbose_name='Удалено',
                                     default=False,
                                     null=False)

    def __str__(self):
        return "{} | {}".format(self.title, self.author_id)

    class Meta:
        app_label = "webapp"
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.is_deleted = True
        self.save()
