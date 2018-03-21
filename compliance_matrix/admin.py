from django.contrib import admin

# Register your models here.
from .models import ComplianceMatric, EHSProjectApplicabliltyStatusReport



#=======CLASS START HERE======================

class ComplianceMatricAdmin(admin.ModelAdmin):
    list_display = ('Program_Name','Type', 'category', 'frequency', 'building_Number','EHS_Person')
    list_filter = ('Type','category','status')
    save_as = True
    save_on_top = True
    change_list_template = 'change_list_graph.html'


class EHSProjectApplicabliltyStatusReportAdmin(admin.ModelAdmin):
    list_display = ('Individual_Responsible','Program_in_Place', 'Ranking')
    list_filter = ('Type','category','status')
    save_as = True
    save_on_top = True
    change_list_template = 'change_list_graph.html'


# Register your models here.  
admin.site.register(ComplianceMatric, ComplianceMatricAdmin)
admin.site.register(EHSProjectApplicabliltyStatusReport, EHSProjectApplicabliltyStatusReportAdmin)