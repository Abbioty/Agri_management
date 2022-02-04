from django.contrib import admin
from .models import Exchange


# Register your models here.


class ExchangeAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Exchange, ExchangeAdmin)
from django.contrib import admin

# Register your models here.
