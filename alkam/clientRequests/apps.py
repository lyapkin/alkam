from django.apps import AppConfig
from django.db.models.signals import post_save





class ClientrequestsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'clientRequests'
    verbose_name = 'запросы звонков и коммерческих предложений'

    def ready(self):
        from .signals import request_save_handlers
        from .models import Call, CommercialOffer
        post_save.connect(
            request_save_handlers.send_mail_on_create,
            sender=Call,
            weak=False,
            dispatch_uid='CallModelFromClientRequestsApp'
        )

        post_save.connect(
            request_save_handlers.send_mail_on_create,
            sender=CommercialOffer,
            weak=False,
            dispatch_uid='CommercialOfferModelFromClientRequestsApp'
        )
