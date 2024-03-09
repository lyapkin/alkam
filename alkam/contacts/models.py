from django.db import models

# Create your models here.
class Address(models.Model):
    region = models.CharField("регион", max_length=50)
    city = models.CharField("город", max_length=50)
    address = models.CharField("адрес", max_length= 50)
    map = models.TextField(max_length=500, blank=True, null=True, verbose_name="Код яндекс карты")

    def __str__(self):
        return f"{self.region}, {self.city}, {self.address}"
    
    class Meta:
        verbose_name = "адрес"
        verbose_name_plural = "адреса"


class TelphoneNumber(models.Model):
    number = models.CharField("номер телефона", max_length=20, unique=True)

    def __str__(self):
        return self.number
    
    class Meta:
        verbose_name = "номер телефона"
        verbose_name_plural = "номера телефонов"


class Email(models.Model):
    email = models.EmailField("адрес электронной почты", max_length=254)

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = "адрес электронной почты"
        verbose_name_plural = "адреса электронной почты"


class Department(models.Model):
    name = models.CharField("название отдела", max_length=30, unique=True)
    telephone_number = models.ForeignKey(TelphoneNumber, null=True, on_delete=models.SET_NULL,
                                         verbose_name="телефон отдела", related_name="departments")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "отдел"
        verbose_name_plural = "отделы"