from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    """ Welcome Page """
    return render(request, "hello/index.html")


def resources(request):
    """ Resources Page """
    return render(request, "hello/resources.html")

def roadmap(request):
    """ Roadmap Page """
    return render(request, "hello/roadmap.html")

def references(request):
    """ References Page"""
    return render(request, "hello/references.html")

    
def contact(request):
    """ Contact Page """
    return render(request, "hello/contact.html")
