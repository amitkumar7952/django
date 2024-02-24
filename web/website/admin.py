from django.contrib import admin
from .models import Contact
from .models import Services
class contactadmin(admin.ModelAdmin):
    list_display=('name','email','phone')
    search_fields=('name',)
# Register your models here.
admin.site.register(Contact,contactadmin)
admin.site.register(Services)