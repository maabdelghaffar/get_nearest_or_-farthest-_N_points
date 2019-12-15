from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.contrib.gis.db.models.functions import Distance
from my_nearest_points.models import Points
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos import Point
from django.http import JsonResponse
from django.core.serializers import serialize
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
import json
import logging
from decimal import *
from django.contrib.auth.models import User
from datetime import datetime


# Get an instance of a logger
logger = logging.getLogger('app-logger')


def mylogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
    return render(request, 'login.html')

def getpoints(request):

    if request.POST.get('action') == 'post':
        now = datetime.now() # current date and time
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        logger.critical("\n ########## Request was received on %s and the request body was: %s ##########\n"%(date_time, request.body))
        x_input = request.POST.get('xcoordinate')
        y_input = request.POST.get('ycoordinate')
        number_of_points = request.POST.get('inputpoints')
        operation = request.POST.get('operator')
        user_location = Point( [Decimal(x_input), Decimal(y_input)], srid = 3857)
        res = serialize('geojson', Points.objects.annotate(distance=Distance('location', user_location)).order_by(operation)[0:int(number_of_points)],  geometry_field='location', srid=3857, fields=('distance','id'))
        return JsonResponse(json.loads(res), safe=False)

    return render(request, 'results.html')
