from django.contrib import admin

# Register your models here.
from .models import FacilityDatabase


class FacilityDatabaseAdmin(admin.ModelAdmin):
    list_display = ('Full_Name','Title', 'Department', 'Building_Address', 'city','country')
    list_filter = ('city','Department','country')
    save_as = True
    save_on_top = True
    change_list_template = 'change_list_graph_facilities.html'



    # Register your models here.  
admin.site.register(FacilityDatabase, FacilityDatabaseAdmin)
