# Generated by Django 5.0.3 on 2024-03-05 13:29

import article.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='название')),
                ('slug', models.SlugField(unique=True, verbose_name='url')),
            ],
            options={
                'verbose_name': 'категория статьи',
                'verbose_name_plural': 'категории статей',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='заголовок')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='url')),
                ('text', models.TextField(verbose_name='текст статьи')),
                ('image_url', models.ImageField(upload_to=article.utils.upload_to, verbose_name='изображение')),
                ('date', models.DateField(auto_now_add=True, verbose_name='дата')),
                ('categories', models.ManyToManyField(related_name='articles', to='article.articlecategory', verbose_name='Категории статьи')),
            ],
            options={
                'verbose_name': 'статья',
                'verbose_name_plural': 'статьи',
            },
        ),
    ]
