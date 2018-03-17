from django.contrib import admin
from .models import ProjectInformation, Manifest, Compliance

# CUSTOM ADMIN VIEWLAYOUT===========

class ProjectInformationAdmin(admin.ModelAdmin):
    list_display = ('person_Responsible','category','Type','status')
    list_filter =('category','status')
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


#========REGISTERING MODELS================================
admin.site.register(ProjectInformation, ProjectInformationAdmin)
admin.site.register(Manifest, ManifestAdmin)
admin.site.register(Compliance, ComplianceAdmin)

# admin.site.register(Sustainability, SustainabilityAdmin)






# Custom Admin==Filter=================
class StatusManifestListFilter(admin.SimpleListFilter):
    title ='Status'
    parameter_name ='status_category'

    def lookup(self, request, model_admin):
        return (

            ('Not Started', 'Not Started'),
            ('In Progress', 'In Progress'),
            ('Completed', 'Completed',),
            ('Pending Initial Approval', 'Pending Initial Approval'),
            ('Pending Final Approval', 'Pending Final Approval'),
            ('Approved', 'Approved'),
            )

    def queryset(self,request,model_admin):
        if self.value() == 'Approved':
            return queryset.filter(
                Q(status=ProjectInformation.APPROVED)|Q (status=ProjectInformation.PENDING))
        if self.value()=='Completed':
             return queryset.filter(
                Q(status=ProjectInformation.IN_PROGRESS)|Q (status=ProjectInformation.NOT_STARTED))

        if self.value()=='Completed':
             return queryset.filter(
                Q(status=ProjectInformation.PENDING_INITIAL_APPROVAL)|Q (status=Project_Information.FINAL_APPROVAL))







class MANAGEMENTAdmin(admin.ModelAdmin):
    list_display=('title','slug','created','status')



# Customer Admin=====================




fieldsets = (
    (None,{'fieldsets':('name',)}),
    ('File',{'fields':('file','status','source')}),
    ('Permission',{'fields':('public','user',),}),






    )


#----------Dashboard--------------------------

list_filter = ('source',)


#========Addition 15Feb2018 End Here===================

#=============NEW DATABASE CHART CODES BELOW======================================
#from django.http import JsonResponse
#from django.views.generic import View

#=====================New DATABASE==============================
#from rest_framework.views import APIView
#from rest_framework.response import Response

#===================================================

def index(request):
    return render(request,'management/index.html')

#========Addition 15Feb2018 Start Here --  # Generate counts of some of the main objects===================

    num_name=Name.objects.all().count()
    num_manifest=ManifestTrackingNumber.objects.all().count()
    num_building=BuildingAddress.objects.all().count()
    num_vendor=VendorName.objects.all().count()
    num_epa=EPAIDLocation.objects.all().count()
    num_dtsc=SentToDTSC.objects.all().count()
    num_returned=ManifestReturedbyVendor.objects.all().count()
    num_vendor_name=VendorName.objects.filter(status__exact='a').count()

#========Addition 15Feb2018 End Here  ===================
def sign(request):
    return render(request,'management/sign.html')

def form(request):
    return render(request,'management/form.html')


