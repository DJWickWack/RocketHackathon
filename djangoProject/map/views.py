from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def map(request):

    return render(request, 'map/trashtagHTML.html')

def trashtagCSS(request):
    return  render(request, 'map/trashtagCSS.css')

def trashtagAdd(request):
    return render(request, 'map/trashtagAddHTML.html')