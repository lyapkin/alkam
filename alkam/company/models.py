from typing import Iterable
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from io import StringIO
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.is_write = False
        self.text = StringIO()

    def handle_starttag(self, tag, attrs):
        if tag == "p":
            self.is_write = True
        else:
            self.is_write = False

    def handle_endtag(self, tag):
        if tag == "p":
            self.is_write = False
        else:
            self.is_write = True

    def handle_data(self, d):
        if self.is_write:
            self.text.write(d.strip() + " ")

    def get_data(self):
        return self.text.getvalue()

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

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
    preview = models.TextField(max_length=500)

    def __str__(self):
        return f"Проект {self.id}"
    
    class Meta:
        verbose_name = "проект"
        verbose_name_plural = "проекты"  

    def save(self, *args, **kwargs):
        self.preview = strip_tags(self.content).strip()
        super().save(*args, **kwargs)     