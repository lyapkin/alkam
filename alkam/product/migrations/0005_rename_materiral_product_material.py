# Generated by Django 5.0.3 on 2024-03-11 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_productmaterial_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='materiral',
            new_name='material',
        ),
    ]