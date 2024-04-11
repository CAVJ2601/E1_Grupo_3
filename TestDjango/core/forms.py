from django import forms
from django.forms import ModelForm
from .models import Usuario

class DateInput(forms.DateInput):
    input_type = 'date'

class TextInput(forms.TextInput):
    input_type = 'text'

class UsuarioForm(ModelForm):
    
    class Meta:
        model = Usuario
        #fields = ['usuario','nombre','correo','password','fecha_nac','direccion']
        fields = ['usuario','nombre','correo','password','fecha_nac','direccion']
        usuario = forms.CharField(widget=forms.TextInput(attrs={'class':'campo_formulario'}))
        nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'campo_formulario'}))
        correo = forms.CharField(widget=forms.TextInput(attrs={'class':'campo_formulario'}))
        password = forms.CharField(widget=forms.TextInput(attrs={'class':'campo_formulario'}))
        direccion = forms.CharField(widget=forms.TextInput(attrs={'class':'campo_formulario'}))

        widgets = {
            'fecha_nac': DateInput(attrs={'class':'campo_formulario'}),
        }