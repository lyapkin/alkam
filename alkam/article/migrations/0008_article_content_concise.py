# Generated by Django 5.0.3 on 2024-03-07 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_alter_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content_concise',
            field=models.TextField(default='Description', max_length=120, verbose_name='краткое описание статьи'),
        ),
    ]
