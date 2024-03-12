from django.contrib import admin

from .models import *


class CallAdmin(admin.ModelAdmin):
    list_display = ["name", "number", "date"]


class CommercialOfferAdmin(admin.ModelAdmin):
    list_display = ["name", "number", "date"]


admin.site.register(Call, CallAdmin)
admin.site.register(CommercialOffer, CommercialOfferAdmin)
