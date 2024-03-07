from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import *


class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Article
        fields = '__all__'

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    prepopulated_fields = {"slug": ("title",)}
    list_display = ["title", "date"]
    filter_horizontal = ("categories",)


class ArticleCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
