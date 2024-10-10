from django.contrib import admin
from .models import Item

# Register your models here.
@admin.register(Item)
class Items(admin.ModelAdmin):
    list_display = ('name', 'description')
