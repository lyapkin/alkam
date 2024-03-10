from django.db import models

# Create your models here.
class About(models.Model):
    text = models.TextField("текст 2-ого блока 'О компании'")

    def __str__(self):
        return "Второй блок 'О компании'"
    
    class Meta:
        verbose_name = "о компании"
        verbose_name_plural = "о компании"