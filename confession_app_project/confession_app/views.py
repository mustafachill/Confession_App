from django.shortcuts import render

# Create your views here.

def listconfesion(request):
    return render(request,'confession_app/listconfession.html')

def addconfesion(request):
    return render(request,'confession_app/addconfession.html')