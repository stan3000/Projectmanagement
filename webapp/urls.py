from django.urls import path
from. import views

urlpatterns = [
    path('webapp/', views.index, name='index')

]