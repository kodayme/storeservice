from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class fomulario_usuario(UserCreationForm):
    email = forms.EmailField(label='correo',required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')