from django.shortcuts import render, redirect
from . import models
from django.views.decorators.csrf import csrf_exempt #if there is something wrong for CSRF
from django.urls import reverse, reverse_lazy
from confession_app.forms import AddConfessionForm, AddConfessionModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from .forms import LoginForm
from django.contrib.auth.views import LogoutView
from .forms import CustomUserCreationForm

# Create your views here.
#@csrf_exempt
def listconfession(request):
    all_confessions = models.Confession.objects.all()
    confessions_dict = {"confessions":all_confessions}
    return render(request,'confession_app/listconfession.html', context=confessions_dict)
#@csrf_exempt
@login_required(login_url="/login")
def addconfession(request):
    if request.POST:
        message = request.POST["message"]
        if message != "":
            models.Confession.objects.create(username=request.user, message=message)
            return redirect(reverse('confession_app:listconfession'))
        return render(request,'confession_app/addconfession.html')
    else:
        return render(request,'confession_app/addconfession.html')

def addconfessionbyform(request):
    if request.POST:
        form = AddConfessionForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nickname_input"]
            message = form.cleaned_data["message_input"]
            models.Confession.objects.create(nickname=nickname, message=message)
            return redirect(reverse('confession_app:listconfession'))
        else:
            print("error in form")
            return redirect(reverse('confession_app:listconfession'))
    else:
        form = AddConfessionForm()
        return render(request,'confession_app/addconfessionbyform.html',context={"form":form})
    
def addconfessionbymodelform(request):
    if request.POST:
        form = AddConfessionModelForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nickname"]
            message = form.cleaned_data["message"]
            models.Confession.objects.create(nickname=nickname, message=message)
            return redirect(reverse('confession_app:listconfession'))
        else:
            print("error in form")
            return render(request,'confession_app/addconfessionbymodelform.html',context={"form":form})
    else:
        form = AddConfessionModelForm()
        return render(request,'confession_app/addconfessionbymodelform.html',context={"form":form})
    
@login_required
def deleteconfession(request,id):
    confession = models.Confession.objects.get(pk=id)
    if request.user == confession.username:
        models.Confession.objects.filter(id=id).delete()
        return redirect('confession_app:listconfession')

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('confession_app:listconfession')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


#LogoutView.as_view()a
@login_required
def log_out(request):
    return render(request,'confession_app/log_out.html')

def terms(request):
    return render(request,'confession_app/terms.html')



