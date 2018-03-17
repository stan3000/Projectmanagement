from django.contrib import admin

from .models import SustainableReport




#=======CLASS START HERE======================

class SustainableReportAdmin(admin.ModelAdmin):
    list_display = ('building', 'city', 'region', 'Type','Amount_Consumped','unit')
    list_filter = ('Type','city','status')
    save_as = True
    save_on_top = True
    change_list_template = 'change_list_graph_sustainability.html'


# Register your models here.  
admin.site.register(SustainableReport,SustainableReportAdmin)
   

