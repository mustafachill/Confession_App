from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from confession_app.models import Confession

class AddConfessionForm(forms.Form):
    nickname_input = forms.CharField(label="Nickname", max_length=50)
    message_input = forms.CharField(label="Message", max_length=250,widget=forms.Textarea(attrs={"class":"confessionmessage"}))


class AddConfessionModelForm(ModelForm):
    class Meta:
        model = Confession
        fields = ["username","message"]

class LoginForm(forms.Form):
    username = forms.CharField(label='Nickname', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class CustomUserCreationForm(UserCreationForm):
    agree_to_terms = forms.BooleanField(
        required=True,
        label="", 
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
    
    def clean_agree_to_terms(self):
        agree_to_terms = self.cleaned_data.get('agree_to_terms')
        if not agree_to_terms:
            raise forms.ValidationError("You must agree to the terms and conditions to register.")
        return agree_to_terms
