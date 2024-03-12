from typing import Iterable
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from io import StringIO
from html.parser import HTMLParser


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)

# Create your models here.
class About(models.Model):
    text = models.TextField("текст 2-ого блока 'О компании'")

    def __str__(self):
        return "Второй блок 'О компании'"
    
    class Meta:
        verbose_name = "о компании"
        verbose_name_plural = "о компании"


class Project(models.Model):
    preview_image = models.ImageField("изображение, превью", upload_to=upload_to)
    content = RichTextUploadingField("содержание проекта")
    preview = models.TextField('краткое описание проекта', max_length=500)

    def __str__(self):
        return f"Проект {self.id}"
    
    class Meta:
        verbose_name = "проект"
        verbose_name_plural = "проекты"      