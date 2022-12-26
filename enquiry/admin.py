from django.contrib import admin
from enquiry.models import Enquiry

class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('full_name','email','company','description')

admin.site.register(Enquiry, EnquiryAdmin)

# Register your models here.
