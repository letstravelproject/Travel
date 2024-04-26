
from django.contrib import admin
from .models import Guidedetails

class GuideAdmin(admin.ModelAdmin):
    list_display = ['Guidename','Phonenumber','Email','Location','Places_To_Visit','Duration','Price'] # Correct the field name here

admin.site.register(Guidedetails, GuideAdmin)