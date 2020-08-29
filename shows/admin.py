# Register your models here.
from django.contrib import admin
from .models import Shows, availableshows


@admin.register(Shows, availableshows)
class ShowAdmin(admin.ModelAdmin):
    readonly_fields = ('showid',)
