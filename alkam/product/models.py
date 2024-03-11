from django.db import models

# Create your models here.
class Product(models.Model):
    product_category = models.ForeignKey("ProductCategory", on_delete=models.PROTECT, related_name="products", verbose_name="тип продукции")
    supply_condition = models.ForeignKey("ProductSupplyCondition", on_delete=models.PROTECT, related_name="products", verbose_name="состояние поставки")
    alloy_type = models.ForeignKey("AlloyType", on_delete=models.PROTECT, related_name="products", verbose_name="марка сплава")
    standard = models.ForeignKey("ProductStandard", on_delete=models.PROTECT, related_name="products", verbose_name="стандарт продукции")
    material = models.ForeignKey("ProductMaterial", on_delete=models.PROTECT, related_name="products", verbose_name="материал продукции")
    thickness_min = models.DecimalField("нижняя граница толщины, мм", max_digits=4, decimal_places=1)
    thickness_max = models.DecimalField("верхняя граница толщины, мм", max_digits=4, decimal_places=1)
    width_min = models.IntegerField("нижняя граница ширины, мм")
    width_max = models.IntegerField("верхняя граница ширины, мм")
    length_min = models.IntegerField("нижняя граница длины, мм")
    length_max = models.IntegerField("верхняя граница длины, мм")

    def __str__(self):
        return f"""Вид продукции: {self.product_category.name};\
                Марка сплава: {self.alloy_type.name}; 
                Толщина: {self.thickness_min}-{self.thickness_max};
                Ширина: {self.width_min}-{self.width_max};
                Длина: {self.length_min}-{self.length_max}"""
    
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
    standard = models.CharField("название", max_length=50, unique=True)

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