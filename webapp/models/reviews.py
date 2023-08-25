from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    description = models.TextField(max_length=3000,
                                   verbose_name='Текст отзыва')

    user_id = models.ForeignKey(User,
                                verbose_name='Автор отзыва',
                                on_delete=models.CASCADE,
                                default=1,
                                related_name='reviews')

    rating = models.PositiveSmallIntegerField(verbose_name='Оценка пользователя',
                                              validators=[MinValueValidator(0),
                                                          MaxValueValidator(10)])
    book_id = models.ForeignKey('webapp.Book',
                                verbose_name='Книга',
                                on_delete=models.CASCADE,
                                related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Время создания отзыва')

    def __str__(self):
        return "{} | {}".format(self.description, self.user_id)

    class Meta:
        app_label = "webapp"
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
