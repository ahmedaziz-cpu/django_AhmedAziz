from django.contrib import admin

from .models import Alumne,Professor


# Register your models here.
@admin.register(Alumne)
class alumnes(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'edat' ,'genere','curs','moduls','tutor','id')

@admin.register(Professor)
class professors(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'edat' ,'genere','curs','moduls','tutor')












