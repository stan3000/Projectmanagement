"""
from django.contrib import admin

#Register your models here.
from .models import Compliance_matrix, Sustainable_report, Manifest,Compliance,Compliance_matrix

# Register your models here.  




# CUSTOM ADMIN VIEWLAYOUT===========

class Project_informationAdmin(admin.ModelAdmin):
    list_display = ('person_Responsible','category','Type','status')
    list_filter =('Type','category','status')
    # search_fields =('category','status')
    save_as = True
    save_on_top = True
    change_list_template = 'change_list_graph.html'


class ManifestAdmin(admin.ModelAdmin):
    list_display = ('Manifest_Signatory','Building_Address','Vendor_Name','EPA_ID_Location','Date_Generator_Sgned','Date_to_DTSC')
    list_filter =('Date_Generator_Sgned','Vendor_Name')
    search_fields =('Type','category','status')
    # search_fields =('category','status') ADDED AFTER GRAGH WORKED = 3/2/2018 -Worked
    save_as = True
    save_on_top = True
    change_list_template = 'change_list_graph.html'


class ComplianceAdmin(admin.ModelAdmin):
    list_display = ('Individual_Responsible','agency','description','Type','start_Date','due_Date', 'status')
    list_filter =('Type','category','category')
    # search_fields =('agency','body') ADDED AFTER GRAGH WORKED = 3/2/2018 - worked
    save_as = True
    save_on_top = True
    change_list_template = 'change_list_graph.html'

#=================COMPLIANCE METRIX================================================


class Compliance_MatrixAdmin(admin.ModelAdmin):
    list_display = ('Program_Name','Type', 'category', 'frequency', 'building','EHS_Person')
    list_filter = ('Type','category','status')
    save_as = True
    save_on_top = True
    change_list_template = 'change_list_graph.html'


#=======Sustainable_Report======================

class Sustainable_ReportAdmin(admin.ModelAdmin):
    list_display = ('building', 'city', 'region', 'Type','Amount_Consumped','unit')
    list_filter = ('Type','category','status')
    save_as = True
    save_on_top = True
    change_list_template = 'change_list_graph.html'



admin.site.register(Sustainable_Report,Sustainable_ReportAdmin)
admin.site.register(Project_information, Project_informationAdmin)
admin.site.register(Manifest, ManifestAdmin)
admin.site.register(Compliance, ComplianceAdmin)
admin.site.register(Compliance_matrix, Compliance_matrixAdmin)

"""