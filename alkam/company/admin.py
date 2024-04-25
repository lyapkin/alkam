from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import *


class AboutAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = About
        fields = '__all__'


class AboutAdmin(admin.ModelAdmin):
    form = AboutAdminForm

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    

class CooperationAdminForm(forms.ModelForm):
    metaltraders = forms.CharField(widget=CKEditorUploadingWidget())
    enterprises = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Cooperation
        fields = '__all__'


class CooperationAdmin(admin.ModelAdmin):
    form = CooperationAdminForm

    # def has_add_permission(self, request, obj=None):
    #     return False
    
    def has_delete_permission(self, request, obj=None):
        return False


class SpecialOfferDescriptionAdmin(admin.ModelAdmin):
    # def has_add_permission(self, request, obj=None):
    #     return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    

class SpecialOffersAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = SpecialOffers
        fields = '__all__'


class SpecialOffersAdmin(admin.ModelAdmin):
    form = SpecialOffersAdminForm

    # def has_add_permission(self, request, obj=None):
    #     return False
    
    # def has_delete_permission(self, request, obj=None):
    #     return False
    

class ProjectAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Project
        fields = '__all__'

class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm





admin.site.register(About, AboutAdmin)
admin.site.register(Cooperation, CooperationAdmin)
admin.site.register(SpecialOfferDescription, SpecialOfferDescriptionAdmin)
admin.site.register(SpecialOffers, SpecialOffersAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register([Slider1, Slider2])