from django.contrib import admin

# Register your models here.
from .models import Shop

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'store_name')