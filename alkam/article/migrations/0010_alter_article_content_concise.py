# Generated by Django 5.0.3 on 2024-03-12 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_alter_article_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content_concise',
            field=models.TextField(max_length=120, verbose_name='краткое описание статьи'),
        ),
    ]