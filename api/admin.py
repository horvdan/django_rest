from api.models import Currency
from django.contrib import admin

# Register your models here.
class CurrencyAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name_plural = "Currencies"

admin.site.register(Currency, CurrencyAdmin)
