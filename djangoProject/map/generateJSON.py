from django.db import models
from map.models import TrashTag
from django.core import serializers

trashtags = TrashTag.objects.all()
structure = serializers.serialize('json', trashtags)

file = open("../static/map/output.json", "w")
file.write(structure)
file.close()