from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home.html", {'lol': 'hue hue hue'})
# Create your views here.
