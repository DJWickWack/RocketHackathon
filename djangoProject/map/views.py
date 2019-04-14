from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from map.models import TrashTag
from django.core import serializers


# Create your views here.
def map(request):

    return render(request, 'map/trashtagHTML.html')

def trashtagCSS(request):
    return  render(request, 'map/trashtagCSS.css')




def trashtagUpdate(request):


    trashtags = TrashTag.objects.all()
    structure = serializers.serialize('json', trashtags)

    file = open("static/map/output.json", "w")
    file.write(structure)
    file.close()

    return HttpResponse("JSON generated!")