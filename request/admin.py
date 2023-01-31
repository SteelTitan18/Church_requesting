from django.contrib import admin
from request.models import Church_request

class Request_listAdmin(admin.ModelAdmin):
    list_display = ('customer', 'start_date', 'end_date', 'hours')

admin.site.register(Church_request, Request_listAdmin)
