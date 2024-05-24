from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import BusinessUser

@admin.register(BusinessUser)
class BusinessUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'role', 'created_at', 'updated_at')
    search_fields = ('username', 'email', 'role')
