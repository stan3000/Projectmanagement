from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def aboutus(request):
    return HttpResponse ("<H2> Thanks you very much Stanley Njoku !</H2>")
