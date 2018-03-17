from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    return HttpResponse ("<H2> HEY! Welcome to Project Management!</H2>")
    template = loader.get_template('myproject/index.html')
    context = {
        ' '
    }


