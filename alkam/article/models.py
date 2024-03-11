from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from .utils import upload_to


# Create your models here.
class Article(models.Model):
    title = models.CharField("заголовок", max_length=100, unique=True)
    slug = models.SlugField("url", max_length=100, unique=True)
    content = RichTextUploadingField("текст статьи")
    content_concise = models.TextField("краткое описание статьи", max_length=120, default="Description")
    image_url = models.ImageField("изображение", upload_to=upload_to)
    date = models.DateField("дата", auto_now_add=True)
    categories = models.ManyToManyField("ArticleCategory", related_name="articles", verbose_name="Категории статьи")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "статья"
        verbose_name_plural = "статьи"


class ArticleCategory(models.Model):
    name = models.CharField("название", max_length=50, unique=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "категория статьи"
        verbose_name_plural = "категории статей"



    