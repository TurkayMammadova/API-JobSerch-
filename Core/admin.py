from django.contrib import admin
from .models import Category,Company,ADS

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name","id"]

class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name"]
  
class ADSAdmin(admin.ModelAdmin):
    list_display = ["name"]
  
  
admin.site.register(Category,CategoryAdmin)
admin.site.register(Company,CompanyAdmin)
admin.site.register(ADS,ADSAdmin)
