from django.contrib import admin
from service.models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'auther', 'service_desc')


admin.site.register(Service,ServiceAdmin)
