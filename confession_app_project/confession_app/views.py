from django.shortcuts import render, redirect
from . import models
from django.views.decorators.csrf import csrf_exempt #if there is something wrong for CSRF
from django.urls import reverse
# Create your views here.
#@csrf_exempt
def listconfession(request):
    all_confessions = models.Confession.objects.all()
    confessions_dict = {"confessions":all_confessions}
    return render(request,'confession_app/listconfession.html', context=confessions_dict)
#@csrf_exempt
def addconfession(request):
    if request.POST:
        nickname = request.POST["nickname"]
        message = request.POST["message"]
        models.Confession.objects.create(nickname=nickname, message=message)
        return redirect(reverse('confession_app:listconfession'))
    else:
        return render(request,'confession_app/addconfession.html')