from django.contrib import admin
from .models import *


class ExpertAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstName', 'lastName')
    list_display_links = ('id', 'firstName', 'lastName')
    search_fields = ('id', 'firstName', 'lastName')


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstName', 'lastName')
    list_display_links = ('id', 'firstName', 'lastName')
    search_fields = ('id', 'firstName', 'lastName')


admin.site.register(Expert, ExpertAdmin)
admin.site.register(Doctor, DoctorAdmin)
