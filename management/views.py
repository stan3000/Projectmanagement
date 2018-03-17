from django.shortcuts import render

#========Addition 15Feb2018 Start Here===================

from. models import ProjectInformation, Manifest, Compliance
#========Addition 15Feb2018 End Here===================

#=============NEW DATABASE CHART CODES BELOW======================================
#from django.http import JsonResponse
#from django.views.generic import View

#=====================New DATABASE==============================
#from rest_framework.views import APIView
#from rest_framework.response import Response

#===================COUNT================================

def index(request):
    return render(request,'management/index.html')
    num_compliance=Compliance.objects.all().count()
    num_manifest=Manifest.objects.all().count()

    return render(
        request,
        'management/index.html',
        context={'num_manifest':num_manifest,'num_compliance':num_compliance},   

      )

#========Addition 15Feb2018 Start Here --  # Generate counts of some of the main objects===================
   

#========Addition 15Feb2018 End Here  ===================
def sign(request):
    return render(request,'management/sign.html')

def form(request):
    return render(request,'management/form.html')

#=============NEW DATABASE CHART CODES BELOW======================================


#class HomeView(View):
	#def get(self,request,*args,**kwargs):
		#return render(request,'charts.html',{"customers":10})


#def get_data(request, * args, **kwargs):
	#data ={
       # "sales":100,
       # "customers": 10,


	#}
	#return JsonResponse(data)


	#=========NEW DATABASE====================================================

#class ChartData(APIView):
   
   # authentication_classes = []
   # permission_classes = []

   # def get(self, request, format=None):
      #  data={
          #   "sales":100,
           #  "customers": 10,

      # }
     #  return Response(data)