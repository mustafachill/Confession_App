from django.shortcuts import render, redirect, get_object_or_404
from . import models
from django.views.decorators.csrf import csrf_exempt #if there is something wrong for CSRF
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from .forms import LoginForm
from django.contrib.auth.views import LogoutView
from .forms import CustomUserCreationForm
from .models import Confession


# Create your views here.
def listconfession(request):
    all_confessions = Confession.objects.all()
    confessions_dict = {"confessions": all_confessions}
    return render(request, 'confession_app/listconfession.html', context=confessions_dict)

def like_confession(request, confession_id):
    if request.method == 'POST':
        confession = get_object_or_404(Confession, id=confession_id)
        if request.user in confession.dislikes.all():
            confession.dislikes.remove(request.user)
        if request.user not in confession.likes.all():
            confession.likes.add(request.user)
        else:
            confession.likes.remove(request.user)
    return redirect('confession_app:listconfession')

@login_required
def dislike_confession(request, confession_id):
    if request.method == 'POST':
        confession = get_object_or_404(Confession, id=confession_id)
        if request.user in confession.likes.all():
            confession.likes.remove(request.user)
        if request.user not in confession.dislikes.all():
            confession.dislikes.add(request.user)
        else:
            confession.dislikes.remove(request.user)
    return redirect('confession_app:listconfession')


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