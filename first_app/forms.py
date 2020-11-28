from django import forms
from django.core import validators
from .models import User


class FormName(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    mail = forms.EmailField()

    class Meta:
        model = User
        fields = '__all__'
        



class NewUserForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    
    def clean(self):
        all_clean_data = super().clean()
        name = all_clean_data['name']
        password = all_clean_data['password']


class FormSearch(forms.Form):

    doctor = forms.CharField()
    paciente = forms.CharField()

    def clean(self):
        all_clean_data = super().clean()
        doctor = all_clean_data['doctor']
        paciente = all_clean_data['paciente']

class Loadfrom(forms.Form):

    archivo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control', 'type' : 'text'}))
    paciente = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control', 'type': 'text'}))
    edad = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control', 'type' : 'text'}))

    def clean(self):
        all_clean_data = super().clean()
        archivo = all_clean_data['archivo']
        paciente = all_clean_data['paciente']
        edad = all_clean_data['edad']

    


