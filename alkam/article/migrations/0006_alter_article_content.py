# Generated by Django 5.0.3 on 2024-03-06 09:54

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_remove_article_content_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='текст статьи'),
        ),
    ]
