from django.contrib import admin
from request.models import ChurchRequest

class Request_listAdmin(admin.ModelAdmin):
    list_display = ('customer', 'start_date', 'end_date', 'hours')

admin.site.register(ChurchRequest, Request_listAdmin)
