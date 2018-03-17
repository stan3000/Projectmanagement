from django.urls import path
from. import views

urlpatterns = [
    path('safety/', views.aboutus, name='aboutus')

]