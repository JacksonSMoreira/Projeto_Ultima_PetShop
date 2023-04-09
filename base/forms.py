from django import forms
from base.models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']

class ReservaForm(forms.Form):
    nomepet = forms.CharField()
    telefone = forms.CharField()
    dia = forms.DateField()
    mensagem = forms.CharField(widget=forms.Textarea)
