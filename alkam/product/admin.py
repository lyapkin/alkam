from django.contrib import admin

from .models import *



class ProductCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

class AlloyTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(ProductCategory, ProductCategoryAdmin)
admin.site.register(AlloyType, AlloyTypeAdmin)
admin.site.register([
    Product,
    ProductSupplyCondition,
    ProductStandard,
    ProductMaterial
])