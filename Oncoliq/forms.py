from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Comentario

class formSetLaboratorio (forms.Form):
    laboratorio = forms.CharField(max_length=30)
    operario = forms.CharField(max_length=30)
    email = forms.EmailField()
    equipo = forms.CharField(max_length=30)
    fecha = forms.DateField()
    resultado = forms.CharField(max_length=30)

class formSetMedico (forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    institucion = forms.CharField(max_length=30)
    informe = forms.CharField(max_length=200)
    mamografia = forms.CharField(max_length=30)

class formSetPaciente(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class UserEditForm(UserChangeForm):
    username = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Username"}))
    email = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Email"}))
    first_name = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"First Name"}))
    last_name = forms.CharField(widget= forms.TextInput(attrs={"placeholder":"Last Name"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields}

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label ="", widget= forms.PasswordInput(attrs={"placeholder":"Old password"}))
    new_password1 = forms.CharField(label ="", widget= forms.PasswordInput(attrs={"placeholder":"New password"}))
    new_password2 = forms.CharField(label ="", widget= forms.PasswordInput(attrs={"placeholder":"Confirm new password"}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'newpassword2']
        help_texts = {k:"" for k in fields}

class avatarForm(forms.Form):
    avatar = forms.ImageField()

class FormularioComentario(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ('nombre', 'mensaje')
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'mensaje' : forms.Textarea(attrs={'class': 'form-control'}),
        }