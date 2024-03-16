from django.db import models

# Create your models here.
class Product(models.Model):
    product_category = models.ForeignKey("ProductCategory", on_delete=models.PROTECT, related_name="products", verbose_name="тип продукции")
    supply_condition = models.ForeignKey("ProductSupplyCondition", on_delete=models.PROTECT, related_name="products", verbose_name="состояние поставки", null=True, blank=True)
    alloy_type = models.ForeignKey("AlloyType", on_delete=models.PROTECT, related_name="products", verbose_name="марка сплава")
    standard = models.ForeignKey("ProductStandard", on_delete=models.PROTECT, related_name="products", verbose_name="стандарт продукции", null=True, blank=True)
    material = models.ForeignKey("ProductMaterial", on_delete=models.PROTECT, related_name="products", verbose_name="материал продукции")
    thickness = models.CharField("верхняя граница толщины, мм", max_length=30, null=True, blank=True)
    width = models.CharField("верхняя граница ширины, мм", max_length=30, null=True, blank=True)
    length = models.CharField("верхняя граница длины, мм", max_length=30, null=True, blank=True)

    def __str__(self):
        return f"""Вид продукции: {self.product_category.name};\
                Марка сплава: {self.alloy_type.name}; 
                Толщина: {self.thickness};
                Ширина: {self.width};
                Длина: {self.length}"""
    
    class Meta:
        verbose_name = "продукция"
        verbose_name_plural = "продукция"


class ProductCategory(models.Model):
    name = models.CharField("название", max_length=50, unique=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "тип продукции"
        verbose_name_plural = "типы продукции"


class AlloyType(models.Model):
    name = models.CharField("название", max_length=50, unique=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "марка сплава"
        verbose_name_plural = "марки сплава"


class ProductMaterial(models.Model):
    name = models.CharField("название", max_length=50, unique=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "материал продукции"
        verbose_name_plural = "материалы продукции"


class ProductStandard(models.Model):
    standard = models.CharField("название", max_length=128, unique=True)

    def __str__(self):
        return self.standard
    
    class Meta:
        verbose_name = "стандарт продукции"
        verbose_name_plural = "стандарты продукции"


class ProductSupplyCondition(models.Model):
    name = models.CharField("название", max_length=50, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "состояние поставки"
        verbose_name_plural = "состояния поставки"