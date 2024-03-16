import logging
from smtplib import SMTPAuthenticationError, SMTPException
from django.core.mail import send_mail
from ..models import *

# print(__name__)
# logger = logging.getLogger(__name__)
# print(logger)

def send_mail_on_create(sender, instance=None, created=False, **kwargs):
    pass
    # if created:
    #     subject = (f'Запрос звонка на номер {instance.number}' 
    #                if sender is Call
    #                else f'Запрос коммерческого предложения {instance.company_name} {instance.product_details}')
    #     message = (f'Имя: {instance.name}\n' +
    #                f'Номер телефона: {instance.number}\n' +
    #                f'Комментарий: {instance.comment}\n'
    #                 if sender is Call
    #                 else f'Контактное лицо: {instance.name}\n' +
    #                      f'Номер телефона: {instance.number}\n' +
    #                      f'Вид деятельности: {instance.activity_type}\n' +
    #                      f'Название предприятия: {instance.company_name}\n' +
    #                      f'Продукт: {instance.product_details}\n' +
    #                      f'Комментарий: {instance.comment}')
    #     try:
    #         send_mail(
    #             subject,
    #             message,
    #             'bronabro@mail.ru',
    #             ['d_mal@mail.ru'],
    #             fail_silently=False
    #             )
    #     except Exception as e:
    #         logger.error(e)


