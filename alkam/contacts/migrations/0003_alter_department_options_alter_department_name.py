# Generated by Django 5.0.3 on 2024-03-09 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_alter_telphonenumber_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'verbose_name': 'отдел', 'verbose_name_plural': 'отделы'},
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=30, unique=True, verbose_name='название отдела'),
        ),
    ]
