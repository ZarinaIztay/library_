# Generated by Django 4.2.4 on 2023-08-24 14:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='Имя автора')),
                ('last_name', models.CharField(max_length=200, verbose_name='Фамилия автора')),
            ],
            options={
                'verbose_name': 'Автор книги',
                'verbose_name_plural': 'Авторы книг',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название книги')),
                ('description', models.TextField(max_length=3000, verbose_name='Описание книги')),
                ('publication_date', models.DateField(verbose_name='Дата публикации')),
                ('deleted_at', models.DateTimeField(default=None, null=True, verbose_name='Дата удаления')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Удалено')),
                ('author_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='webapp.author', verbose_name='Автор книги')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Жанр книги')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=3000, verbose_name='Текст отзыва')),
                ('rating', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], verbose_name='Оценка пользователя')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания отзыва')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='webapp.book', verbose_name='Книга')),
                ('user_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='Автор отзыва')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.CreateModel(
            name='Favourites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourites', to='webapp.book', verbose_name='Книга')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourites', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Избранное',
                'verbose_name_plural': 'Избранное',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='genre_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='webapp.genre', verbose_name='Жанр книги'),
        ),
    ]
