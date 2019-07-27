from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.


def index(request):

    r = requests.get('http://api.open-notify.org/iss-now.json?callback=?')

    lat = r.text[80:87]
    lon = r.text[105:113]

    context = {'lat': lat, 'lon': lon}

    return render(request, 'location/base.html', context)
