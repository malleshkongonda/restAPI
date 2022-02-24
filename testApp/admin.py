from django.contrib import admin
from testApp.models import AddressBook


# Register your models here.

class AddressAdmin(admin.ModelAdmin):
    list_display = ['long_position', 'lat_position']
admin.site.register(AddressBook, AddressAdmin)
 