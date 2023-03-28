'''from .models import nota
from django import forms
from django.forms import ModelForm

class NotaForm(ModelForm):
    nota_titulo = forms.CharField(label='titulo', widget=forms.TextInput(attrs={'class': "form-control form-control-lg"}))
    nota_conteudo = forms.TextInput(attrs={'class': "form-control"})
    class Meta:
        model = nota
        fields = ['titulo', 'conteudo']'''