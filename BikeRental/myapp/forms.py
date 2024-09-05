from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . models import reg,Student,CustomUser

class MyStdRegFrm(forms.ModelForm):
    class Meta:
        model =Student
        fields = "__all__"


class empregfrm(forms.ModelForm):
    class Meta:
        model = reg
        fields = "__all__"

class UserRegFrm(UserCreationForm):
       username=forms.CharField(
           label=("Username"),
            widget=forms.TextInput(attrs={"class": "form-control"})
       )
       class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name','email','mobile')


class UserlogFrm(AuthenticationForm):
    password=forms.CharField(
            label=("Enter Password"),
            widget=forms.PasswordInput(attrs={"class": "form-control"})
       )
    

