from typing import Iterable
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

from io import StringIO
from html.parser import HTMLParser


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

# Create your models here.
class About(models.Model):
    text = models.TextField("текст 2-ого блока 'О компании'")

    def __str__(self):
        return "'О компании'"
    
    class Meta:
        verbose_name = "о компании"
        verbose_name_plural = "о компании"


class Cooperation(models.Model):
    description = models.TextField('"Сотрудничество", первый экран')
    metaltraders = RichTextField("металлотрейдерам")
    enterprises = RichTextField(verbose_name="предприямтиям")

    def __str__(self):
        return "'Сотрудничество'"
    
    class Meta:
        verbose_name = "сотрудничество"
        verbose_name_plural = "сотрудничество"


class SpecialOfferDescription(models.Model):
    description = models.TextField()

    def __str__(self):
        return "'Спецпредложения' описание (первый экран)"
    
    class Meta:
        verbose_name = "первый экран раздела 'Спецпредложения'"
        verbose_name_plural = "первый экран раздела 'Спецпредложения'"


class SpecialOffers(models.Model):
    title = models.CharField('заголовок спецпердложения', max_length=100, unique=True)
    text = models.TextField("спецпредложение")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "спецпредложение"
        verbose_name_plural = "спецпредложения"


class Project(models.Model):
    preview_image = models.ImageField("изображение, превью", upload_to=upload_to)
    content = RichTextUploadingField("содержание проекта")
    preview = models.TextField('краткое описание проекта', max_length=500)

    def __str__(self):
        return f"Проект {self.id}"
    
    class Meta:
        verbose_name = "проект"
        verbose_name_plural = "проекты"      