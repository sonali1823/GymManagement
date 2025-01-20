from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Enquiry)
admin.site.register(Equipment)
admin.site.register(Plan)
admin.site.register(Member)
