from django.urls import path
from. import views

#==========Database========================================

#from.views import HomeView, get_data
#==========Database========================================

urlpatterns = [
     path('',views.index, name ='index'),
     path('sign/', views.sign, name='sign'),
     path('form/', views.form, name='form'),
     #===DASH
    
   
    

     
   ]