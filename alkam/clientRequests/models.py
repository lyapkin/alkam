from django.db import models



class Call(models.Model):
    name = models.CharField("контактное лицо", max_length=100)
    number = models.CharField("номер телефона", max_length=20)
    comment = models.TextField("комментарий", blank=True, null=True)
    date = models.DateTimeField("дата", auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.number}'
    
    class Meta:
        verbose_name = "запрос звонка"
        verbose_name_plural = "запросы звонков"


class CommercialOffer(Call):
    product_details = models.CharField("продукт", max_length=50)
    activity_type = models.CharField("вид деятельности", max_length=50, null=True, blank=True)
    company_name = models.CharField("наименование предприятия или И.П.", max_length=100)


    def __str__(self):
        return f'{self.id} {self.product_details} {self.company_name}'
    
    class Meta:
        verbose_name = "запрос коммерческого предложения"
        verbose_name_plural = "запросы коммерческого предложения"



    