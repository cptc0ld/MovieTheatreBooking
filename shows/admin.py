# Register your models here.
from django.contrib import admin
from .models import Shows


@admin.register(Shows)
class ShowAdmin(admin.ModelAdmin):
    readonly_fields = ('showid',)
