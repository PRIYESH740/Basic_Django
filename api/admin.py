from django.contrib import admin
from .models import *

class ServiceAdmin(admin.ModelAdmin):
    list_display=('service_icon','service_title','service_des')

admin.site.register(Service,ServiceAdmin)
admin.site.register(TeamMember)
admin.site.register(FoodItem)
admin.site.register(Homepage)
admin.site.register(ContactFormEnquiry)
admin.site.register(Order)
