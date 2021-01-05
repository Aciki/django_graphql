from django.contrib import admin
from .models import P_info

# Register your models here.

class P_infoAdmin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'club_name','rating')

admin.site.register(P_info,P_infoAdmin)
