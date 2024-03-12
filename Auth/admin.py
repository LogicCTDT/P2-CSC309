from django.contrib import admin
from Auth.models import Contact
from Meeting.admin import ContactAdmin

# Register your models here.
admin.site.register(Contact, ContactAdmin)